from network import WLAN
import machine
wlan = WLAN(mode=WLAN.STA)

nets = wlan.scan()
for net in nets:
    if net.ssid == 'TESTES-NASH':
        print('Network found!')
        wlan.connect(net.ssid, auth=(net.sec, 'nashifce8556'), timeout=5000)
        while not wlan.isconnected():
            machine.idle() # save power while waiting
        print('WLAN connection succeeded!')
        break

wlan.init(mode=WLAN.STA)
# configuration below MUST match your home router settings!!
wlan.ifconfig(config=('192.168.178.117', '255.255.255.0', '192.168.178.1', '8.8.8.8'))

print("ready!")
