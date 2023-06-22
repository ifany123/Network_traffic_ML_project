import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import warnings
import csv
import time, datetime
warnings.filterwarnings('ignore')
start = datetime.datetime.now()

def clurst(center_num,file):
    
    df = pd.read_csv(file)
    X = df[['SrcIp', 'DstIp', 'ProtoType', 'SrcPort', 'DstPort', 'TotalLen']]
    src_ips = df['SrcIp'].values

    for col in ['SrcIp', 'DstIp']:
        X[col] = X[col].apply(lambda x: sum([int(x.split('.')[i])*(256**(3-i)) for i in range(4)]))

    kmeans = KMeans(n_clusters=center_num, random_state=0).fit(X)
    labels = kmeans.labels_
    centers = kmeans.cluster_centers_

    cout=0.0
    total=0.0

    for center in centers:
        total+=1
        center_ip = '.'.join([str(int((center[0]//(256**i))%256)) for i in range(3,-1,-1)])
        if center_ip in src_ips:
            #print(f'Controllor Ip: {center_ip}')
            cout+=1

    print(f'{cout} in {total} is current, accuracy is {(cout/total)*100}%')

clurst(3,"example_file.csv")
