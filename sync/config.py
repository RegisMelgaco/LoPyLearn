
import machine
import ubinascii

WIFI_MAC = ubinascii.hexlify(machine.unique_id()).upper()
# Set  the Gateway ID to be the first 3 bytes of MAC address + 'FFFE' + last 3 bytes of MAC address
GATEWAY_ID = WIFI_MAC[:6] + "AABB" + WIFI_MAC[6:12]

SERVER = 'router.eu.thethings.network'
PORT = 1700

NTP = "pool.ntp.org"
NTP_PERIOD_S = 3600

WIFI_SSID = 'TESTES-NASH'
WIFI_PASS = 'nashifce8556'

LORA_FREQUENCY = 868134000
LORA_GW_DR = "SF7BW125" # DR_5
LORA_NODE_DR = 5
