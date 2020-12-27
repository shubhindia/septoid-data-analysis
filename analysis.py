import pandas as pd
df = pd.read_csv("data.txt", index_col=False, header=None)
usable_data= []
for i in df.values:
    if i[2] > "09:16" and i[2] < "15:30":
        usable_data.append(i)
usable_dataframe = pd.DataFrame(usable_data)
j = 0
k = 0
for i in usable_dataframe.values:

    sma14_list = []
    sma30_list = []
    while(j <  14):
        sma14_list.append(i[5])
        j +=1
    sma14_avg = sum(sma14_list) / len(sma14_list)
    j = 0
    k = 0
    while(k < 30):
        sma30_list.append(i[5])
        k +=1
    sma30_avg = sum(sma30_list) / len(sma30_list)
    if sma14_avg > sma30_avg:
        print("{} {} {}".format(i[1], i[2], "BUY"))
    else:
        print("{} {} {}".format(i[1], i[2], "SELL"))
