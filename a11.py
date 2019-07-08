f = open("test.txt",'r')
read = f.readlines()
f.close

for n in read:
    print(n.strip())
