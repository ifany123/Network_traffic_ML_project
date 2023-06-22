import socket
import struct
import time
import csv
import numpy as np
import datetime
import capture_traffic

def socket_send_and_rec(s,msg):
    s.send(msg)
    data=s.recv(1024)
    try:
        #Please note that the order of the data may sometimes vary
        hex_data=hex(data[11])[2:].zfill(2)+hex(data[12])[2:].zfill(2)+hex(data[9])[2:].zfill(2)+hex(data[10])[2:].zfill(2)
        #other order: hex(data[11])[2:].zfill(2)+hex(data[12])[2:].zfill(2)+hex_data=hex(data[9])[2:].zfill(2)+hex(data[10])[2:].zfill(2)
    except:
        hex_data=0
    return hex_data

def write_in_csv_file(f,num,data):
    f.write(str(num+1))
    f.write(',')
    f.write(datetime.datetime.now().strftime('%H:%M:%S'))
    f.write(',')
    f.write(str(data))
    f.write('\n')

# socket parameters
HOST = device_ip
PORT = 502

#modbus paket parameter
TID=b'\x00\x01'
pID=b'\x00\x00'
Length=b'\x00\x06'
slAdd_PA3000=b'\x01'
slAdd_EM1100=b'\x0f'
fcode4=b'\x04'
fcode3=b'\x03'
stReg=b'\x10\x21'
inReg=b'\x00\x00'
req_num=b'\x00\x02'
crc=b'\x34\xc5'

# build socket connection
socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))
msg=TID+pID+Length+slAdd_PA3000+fcode4+stReg+req_num


def ask_and_save_data():
    num=1

    while(True):
        with open(your_filename, 'w', encoding='UTF8', newline='') as f:
            f.write('data_num,time,Iavg')
            f.write('\n')

            timer=1
            stop_time=3600*num
            capture_traffic.cap(stop_time,num)
            while(timer<stop_time):

                #store PA3000 data
                data=socket_send_and_rec(s=socket,msg=msg)
                final_float_data=struct.unpack('!f', bytes.fromhex(data))[0]
                write_in_csv_file(f,(timer),final_float_data)
                print(datetime.datetime.now().strftime('%H:%M:%S'),": store data: ",data)      

                #Please be aware that the conversion method may also vary at times.
                #other method:final_uint32_data=struct.unpack('>i', bytes.fromhex(dEM))[0]
                time.sleep(1) #sleep 1 sec
                timer+=1
                if(timer%4==0): timer+=1
        print("******Round ",num," end. ******")
        num+=1

ask_and_save_data()