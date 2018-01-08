from network import WLAN
wlan = WLAN(mode=WLAN.STA)
wlan.ifconfig(config=('192.168.0.3', '255.255.255.0', '192.168.178.1', '8.8.8.8'))
