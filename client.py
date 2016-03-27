receiveServerData = "[PythonServer]==> "
sendClientData = "[PythonClient]==> "

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

print "[*] Choose your custom username:"
username = raw_input("[+] Username: ")
print "[*] What Is The Address You Would Like To Connect To?"
target_host = raw_input("[+] Target Host: ")
target_port = input("[+] Target Port: ")
print "################"
#target_host = "127.0.0.1"
#target_port = 9999

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host,target_port))

# send some data
print colour.FAIL + "[Me]==> What Did You Have For Breakfast?"
client.send("[Connecting...]==> What Did You Have For Breakfast?")

# receive some data - This Will Confirm If We Have Connected To The Correct Server.
response = client.recv(4096)
print colour.FAIL + response + colour.ENDC

#AUTHENTICATION
if response == "[PythonServer]==> Toast":
    print colour.OKBLUE + "[*] Server Is Valid! You May Continue To Communicate..." + colour.OKGREEN
    print "################"



    #MAIN LOOP
    #ASKS FOR USER INPUT TO BE SENT TO THE SERVER... FROM NOW ON, THE SERVER WILL NOT REPLY.

loop = 1
while (loop < 2):

        send = (raw_input("[Me]==> "))

        #Anti Spam
        if send == "":
            print colour.OKBLUE + "[+] Type Something!" + colour.ENDC

        if send != "":
                client.send(username)
                time.sleep(0.15)
                client.send(send)



else:
    print colour.BOLD + "[*] Server Is Not Valid :(" + colour.ENDC
    sys.exit()
