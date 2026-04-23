import time
import can
from PCANBasic import *

pcan = PCANBasic()

def can_init():
    res = pcan.Initialize(PCAN_USBBUS1,PCAN_BAUD_500K)
    return res
def device_Info():
    return pcan.GetValue(PCAN_USBBUS1,PCAN_DEVICE_ID)

def write_can(channel,msg):
    return pcan.Write(channel,msg)

result = can_init()
print(result)
print(device_Info())
print(f'PCAN status before unint : {pcan.GetStatus(PCAN_USBBUS1)}')

if result == 0:
    msg = TPCANMsg()
    msg.ID = 0x450
    msg.LEN = 8
    msg.MSGTYPE = PCAN_MESSAGE_STANDARD.value
    # for i in range(8):
    #     msg.DATA[i] = i

    for i in range(30):
        for j in range(8):
            msg.DATA[j] = i
        time.sleep(1)
        write_can(PCAN_USBBUS1,msg)
        
    pcan.Uninitialize(PCAN_USBBUS1)
    
else:
    print("Not Connected")


    


    
    