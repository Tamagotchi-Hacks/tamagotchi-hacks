INTERFACE=wlan1
CHANNEL=6
airmon-ng check kill
airmon-ng start $INTERFACE $CHANNEL