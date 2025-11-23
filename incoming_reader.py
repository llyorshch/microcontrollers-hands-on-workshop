import meshtastic
import meshtastic.serial_interface
from pubsub import pub

print("Connecting to the device")
interface = meshtastic.serial_interface.SerialInterface()
print(f"Connected to node: {interface.getMyNodeInfo()['user']['longName']}")

def onReceive(packet, interface):
    try:
        print(f"Received: {packet['decoded']['payload'].decode('utf-8')}")
    except Exception as e:
        print(f"Error decoding payload: {e}")

pub.subscribe(onReceive, "meshtastic.receive")
while True:
    #time.sleep(1000)   
    input("Press Enter to quit...\n")
    break
interface.close()
