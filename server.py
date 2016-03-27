#!/usr/bin/python
myName = "PythonServer"
sendServerData = "[PythonServer]==> "

#COLOURSSS!
class colour:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

import socket
import time
import sys
import threading
import time

#LOGFILE HEADERS WITH TIMESTAMP
timestamp = time.asctime( time.localtime(time.time()) )
str(timestamp)
f = open("log.txt","a") #opens log file with name of "log.txt"
f.write("################\n")
logHeader = "Log For:" + timestamp + "\n"
f.write(logHeader)
f.write("################\n")
f.close()

bind_ip = "0.0.0.0"
bind_port = 9999

# create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the server
server.bind((bind_ip,bind_port))

server.listen(5)

print "[*] Listening on %s and  on port  %d  (for  local  connections)" % (bind_ip,bind_port)
print "[*] For external  connections  or connections  over a  network,"
print "[*] Please use internal or external iPv4 address of this device"
def handle_client(client_socket):

    # print out what the client sends
    request = client_socket.recv(1024)

    if request == "[Connecting...]==> What Did You Have For Breakfast?":
        print colour.FAIL + "%s" % request
        # send back a packet for authentication
        client_socket.send("[PythonServer]==> Toast")
        print colour.FAIL + "[Me]==> Toast" + colour.ENDC
        print "################"

    # MAIN LOOP
    loop = 1
    while (loop < 2):

        request = client_socket.recv(1024)
        clientUsername = request
        receiveClientData = "[%s]==> " % clientUsername

        request = client_socket.recv(1024)
        #LOGFILE
        f = open("log.txt","a") #opens log file with name of "log.txt"
        message = receiveClientData + request + "\n"
        f.write(message)
        f.close()

        #SIMPLE LOG FILE... FOR USE WITH WIFI PINEAPPLE
        #You will have to comment out the lines which write out a timestamp to the logfile.
        # f = open("log.txt","a") #opens log file with name of "log.txt"
        # message = request + "\n"
        # f.write(message)
        # f.close()

        #BUGFIX NO 1
        if request == "":
            print colour.OKBLUE + "Client Disconnected: %s%d" % (addr[0],addr[1]) + colour.ENDC
            sys.exit("Waiting For New Connection...")

        print colour.WARNING + receiveClientData + "%s" % request + colour.ENDC

    client_socket.close()

while True:

    client,addr = server.accept()
    print colour.ENDC + "################"
    print colour.OKBLUE + "[*] Accepted Connection From: %s%d" % (addr[0],addr[1])

    # spin up our client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()
