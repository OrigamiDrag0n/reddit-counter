import csv
from numpy import array
import matplotlib.pyplot as plt
from datetime import datetime

times = []
users = []

with open(r"D:\reddit_users_2.csv",mode = "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        #print(row)
        try:
            users.append(int(row[6][:-2]))
            times.append(datetime(int(row[0][3:]),int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(float(row[5].split("`")[0])), int(float(row[5].split("`")[1][:-1]))))
        except (IndexError, ValueError):
            pass
"""      
times2 = []
users2 = []

with open(r"D:\reddit_dankmemes.csv",mode = "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        #print(row)
        try:
            users2.append(int(row[6][:-2]))
            times2.append(datetime(int(row[0][3:]),int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(float(row[5].split("`")[0])), int(float(row[5].split("`")[1][:-1]))))
        except (IndexError, ValueError):
            pass
"""

times = array(times); users = array(users)
plt.plot(times,users)
plt.ylabel("Number of Active Users")
plt.xlabel("GMT (+0hrs)")
plt.title("Active Users for r/dankmemes")
plt.gcf().autofmt_xdate()

plt.show()
