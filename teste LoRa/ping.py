from network import LoRa
import socket
import time

lora = LoRa(mode=LoRa.LORA)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)

i = 0

while True:
    if s.recv(64) == b'Ping':
        s.send('Pong')
        print("Pong", i)
        i+=1
    time.sleep(5)
