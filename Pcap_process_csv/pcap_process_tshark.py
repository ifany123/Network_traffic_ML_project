import os
import csv

# trans pcap file to csv file
calltshark="tshark"
read="-r"
filename="yourfile.pcap"
process_com="-T fields -e ip.src -e ip.dst -e ip.proto -E separator=, -E occurrence=f"
out_file="youroutfilename.csv"
command=calltshark+" "+read+" "+filename+" "+process_com+" > "+out_file
os.system(command)


# clean datas in csv files
with open(out_file, "r") as infile:
    reader = list(csv.reader(infile))
    # row names
    toAdd = ["SrcIp","DstIp","ProtocolNum"]
    reader.insert(0, toAdd)

with open("proces.csv", "w") as outfile:
    writer = csv.writer(outfile)
    for line in reader:
        if line[0]=="SrcIp": writer.writerow(line)
        elif line[2] == '6' : writer.writerow(line)

infile.close()
outfile.close()


