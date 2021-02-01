names=[]    
n=int(input("Enter the number of entries"))
for i in range(n):
    print(i+1,"Enter Name")
    names.append(input())
s=set(names)
names = list(s)
for x in names:
    print (x)