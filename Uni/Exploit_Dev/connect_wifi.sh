SSID='Riolu-Love'
PASS='HomageToTheDoctor^$^'
INTERFACE='wlan1'
sudo nmcli device wifi connect "$SSID" password "$PASS" ifname "$INTERFACE"
