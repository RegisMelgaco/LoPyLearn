from network import LoRa
import socket
import time

lora = LoRa(mode=LoRa.LORA) # inicia o objeto LoRa no modo LORAWN
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW) # inicia um socket LoRa
s.setblocking(False) # desbloqueia o socket

i = 0

s.send('Ping') # envia dados
print("Ping")

while True:
    if s.recv(64) == b'Pong': # recebe dados e compara
        s.send('Ping')
        print("Ping", i)
        i+=1
    time.sleep(5)

# metodos de autenticação possiveis são ABP e OTAA
# a banda utilizada foi a padrão
