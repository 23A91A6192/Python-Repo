import csv
#open the csv file
f=open("marks.csv", "r")
#create a csv reader object
r=csv.reader(f)
#list of list
data=list(r)
print(data)
titles=data.pop(0)
toppers=[]
t=[]
for i in data:
    s=0
    for j in range(1,len(i)):
        s+=int(i[j])
    print(s)
    if(s>=300):
        toppers.append(i[0])
toppers.sort()
print(toppers)
for k in data:
    if sum(map(int,k[1:]))>=300:
        t.append(k[0])
t.sort()
print(t)