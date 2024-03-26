wifi_device=$1

echo 'Disconnecting from wifi...'
nmcli d disconnect $wifi_device
echo 'Reloading network manager'
nmcli g reload
sleep 3
echo 'Turning off network manager'
nmcli n off
sleep 3
echo 'Turning on network manager'
nmcli n on
echo 'Changing interface mode to auto'
iwconfig $wifi_device mode auto
sleep 3
#iwconfig $wifi_device txpower off
#sleep 3
#iwconfig $wifi_device txpower auto
echo 'Rfkilling wifi'
rfkill block wifi
sleep 3
echo 'Rfkill unblocking wifi'
rfkill unblock wifi
sleep 3
echo 'Restarting networking stack'
systemctl restart networking
iwconfig
echo 'Done!'
