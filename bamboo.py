import csv
#open the csv file
f=open("bambo.csv", "r")
#create a csv reader object
r=csv.reader(f)
#list of list
data=list(r)
#print(data)
titles=data.pop(0)
topper=[]
print("hakerrank 0 star---------")
for i in data:
    if int(i[titles.index("hr_c")])==0:
        print(i[titles.index("name")])
print("codechef 2 star---------")
for j in data:
    if int(j[titles.index("cc_rating")])>=1400 and int(j[titles.index("cc_rating")])<=1599 and (j[titles.index("college")])=='AEC' and (j[titles.index("branch")])=='CSE':
        print(j[titles.index("name")],j[titles.index("roll_number")])
print("leetcode highest---------")
max=0
for k in data:
    s=0
    s+=int(k[titles.index("lc_easy")])+int(k[titles.index("lc_medium")])+int(k[titles.index("lc_hard")])
    if s>max:
        max=s
        name=k[titles.index("name")]
        roll=k[titles.index("roll_number")]
print(max,name,roll)