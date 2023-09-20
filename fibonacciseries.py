#fibonacci series
n=int(input("enter your number: "))
a = 0
b = 1
s = 0
count = 0
print(a,b,sep=" , ",end=" , ")
while count!=n:
    s = a+b
    a = b
    b = s
    count += 1
    print(s,end=" , ")
