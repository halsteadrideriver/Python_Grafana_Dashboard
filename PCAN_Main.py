import time
import can
from PCANBasic import *

pcan = PCANBasic()

def can_init():
    res = pcan.Initialize(PCAN_USBBUS1,PCAN_BAUD_500K)
    return res

# 
# def device_Info():
#     return pcan.GetValue(PCAN_USBBUS1,PCAN_DEVICE_ID)

# def write_can(channel,msg):
#     return pcan.Write(channel,msg)

# result = can_init()
# print(result)
# print(device_Info())
# print(f'PCAN status before unint : {pcan.GetStatus(PCAN_USBBUS1)}')

# if result == 0:
#     msg = TPCANMsg()
#     msg.ID = 0x450
#     msg.LEN = 8
#     msg.MSGTYPE = PCAN_MESSAGE_STANDARD.value
#     # for i in range(8):
#     #     msg.DATA[i] = i

#     for i in range(30):
#         for j in range(8):
#             msg.DATA[j] = i
#         time.sleep(1)
#         write_can(PCAN_USBBUS1,msg)
        
#     pcan.Uninitialize(PCAN_USBBUS1)
    
# else:
#     print("Not Connected")

# PCAN read :
def PCAN_read():
    try:
        while True:
            res = pcan.Read(PCAN_USBBUS1)
            print(f" the res : {res[0]}")
            
            if res[0] == PCAN_ERROR_OK:
                msg = res[1]
                timestamp = res[2]
                
                data_format = " ".join([f'{b:02X}' for b in msg.DATA[:msg.LEN]])
                print(f"ID={msg.ID:03X} , LEN:{msg.LEN} , Data={data_format}")
                
            else:
                print("Error at reading")
                
            time.sleep(0.5)
                
    except KeyboardInterrupt:
        pcan.Uninitialize(PCAN_USBBUS1)
        print("Stopped")
         
print(can_init())

time.sleep(1)

PCAN_read()

            