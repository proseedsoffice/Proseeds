
f1=open("pp.txt", "r+")
string=f1.read(11)
print(string)

print(f1.tell())

f1.seek(0,0)


string=f1.read(11)
print(string)



f1.close()
