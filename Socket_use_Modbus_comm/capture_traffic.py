# for capture traffic flow

import subprocess

call_tshark="& \'C:\\Program Files\\Wireshark\\tshark.exe\'"
interface="-i 4"
auto_stop="-a duration:"

stop_time=5
write_file="-w "
cap_header='cap'
pcap='.pcap'
num=1
format_choose="-F pcap"

def cap(st_time,n):
    cap_name=cap_header+(str)(n)+pcap
    command=call_tshark+" "+interface+" "+auto_stop+(str)(st_time)+" "+write_file+cap_name+" "+format_choose
    subprocess.Popen(["powershell.exe",command])