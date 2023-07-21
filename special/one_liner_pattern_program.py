string = input()
l1 = len(string)

for i in range(l1,0,-1):
    print("%*.*s%-*.*s"%(l1,i,string,l1,i,string))

for i in range(1,l1+1):
    print("%*.*s%-*.*s"%(l1,i,string,l1,i,string))
