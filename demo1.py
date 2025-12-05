#csv eriting
import csv
f=open("demo1output.csv","w",newline="")
#csv.writer()object
w=csv.writer(f)
#iterable (list, tuple)
names=["abc","xyz","pqr"]
w.writerow(names)
titles=["NAME","BRANCH","COLLEGE"]
records=[["vaishu","AIML","AEC"],["Renu","AIML","AEC"],["Ishu","AIML","AEC"]]
w.writerow(titles) #single list
w.writerows(records) #list of list
f.close()