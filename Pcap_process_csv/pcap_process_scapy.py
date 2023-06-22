from scapy.all import *
import csv
import time, datetime

start = datetime.datetime.now()
def process(file):
    capture = rdpcap('yourfile.pcap')
    print(f'There are {len(capture)} packets in total.')
    header=['PcaketID','SrcMAC','DstMAC','SrcIp','DstIp','ProtoType','SrcPort','DstPort','TimeStamp','TotalLen','TCPpayloadLen']
    with open(file,'w') as outputfile:
        writer=csv.writer(outputfile)
        writer.writerow(header)
        for pkt in capture:
            data=[]
            if pkt.haslayer("Ether") and pkt.haslayer("IP") and pkt.haslayer("TCP"):
                data.append(pkt.id)
                data.append(pkt["Ether"].src)
                data.append(pkt["Ether"].dst)
                data.append(pkt["IP"].src)
                data.append(pkt["IP"].dst)
                data.append(pkt["IP"].proto)
                data.append(pkt["TCP"].sport)
                data.append(pkt["TCP"].dport)
                data.append(pkt.time)
                data.append(len(pkt.payload))
                data.append(len(pkt["TCP"].payload))
                # timestamp=pkt.time-pkt.sent_time
                # data.append(timestamp)
                writer.writerow(data)
            else: continue

# Count run time
def count_run_time():
    end = datetime.datetime.now()
    diff = (end - start)
    diff_seconds = int(diff.total_seconds())
    minute_seconds, seconds = divmod(diff_seconds, 60)
    hours, minutes = divmod(minute_seconds, 60)
    print(f'Run time: {hours}:{minutes}:{seconds}')

process(your_out_file_name)

