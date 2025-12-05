# open the file
f=open("example.txt","r")
# use a method called read() to read the data in txt file"
data1=f.read(10)
data2=f.read(5)
print(data1)
print(data2)
f.close()