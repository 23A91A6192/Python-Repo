#f=open("C:\\Users\\Sreenivas\\OneDrive\\Desktop\\certificates\\demo.txt","r")
#print(f.read())
f=open("input.txt","r")
value = int(f.read())
sq=value*value
f1=open("output.txt","w")
f1.write(str(sq))
f1.close()
f.close()