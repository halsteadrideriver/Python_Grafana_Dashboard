import can

# Initialize the PCAN bus on the first USB channel
try:
    bus = can.interface.Bus(interface='pcan', channel='PCAN_USBBUS2')
    
    # Retrieve the unique device number
    dev_num = bus.get_device_number()
    
    print(f"Connected to PCAN! Device Number: {dev_num}")

except can.CanError as e:
    print(f"Failed to connect: {e}")

finally:
    # Ensure the bus is closed properly
    if 'bus' in locals():
        bus.shutdown()