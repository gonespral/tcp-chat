echo "[*] Starting NetCat Server..."
echo "#############################"
sleep 0.2
echo "[*] Which Port Would You Like To Listen On?"
read -p Port: port
echo "[*] Starting... "
netcat -l -p $port
