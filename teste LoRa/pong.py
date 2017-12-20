from network import LoRa
import socket
import time

lora = LoRa(mode=LoRa.LORA)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)

i = 0

s.send('Ping')
print("Ping")

while True:
    if s.recv(64) == b'Pong':
        s.send('Ping')
        print("Ping", i)
        i+=1
    print("perando")
    time.sleep(5)
