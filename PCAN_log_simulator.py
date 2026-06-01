import pandas as pd
import cantools

df = pd.read_csv(r"C:\Users\halstead_rideriver\Downloads\Pre can data Y-axis.csv").to_string(index=False)
# print(df.to_string(index=False))
#print(df)

can_obj = cantools.database.load_file("DBC_Gen3_EOL V1_0.dbc")

def fun1(bytedata):
    data = can_obj.decode_message(frame_id_or_name=615,data=bytedata) # byte literal.
    print(data)
    
hexstring = 'AA 0C A5 0C 87 0C 7B 0C'
byteliteral = bytes.fromhex(hexstring)
    
fun1(byteliteral)
