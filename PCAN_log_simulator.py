import pandas as pd
import cantools

df = pd.read_csv(r"C:\Users\halstead_rideriver\Downloads\Pre can data Y-axis.csv").to_string(index=False)
# print(df.to_string(index=False))
#print(df)

can_obj = cantools.database.load_file("DBC_Gen3_EOL V1_0.dbc")
print(can_obj.decode_message(frame_id_or_name=564,data=b'0x6E|0x32|0x10|0x3C|0x10|0x41|0x20|0x1F'))
