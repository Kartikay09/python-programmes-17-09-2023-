'''
Write a program for the given integers P and X, that display the positive integer pairs (i, j) with satisfy the following conditions.

i + j == P
i XOR j == X
'''
p=int(input())
x=int(input())
a=0
b=0


for i in range(0,p+1):
    a=i
    b=p-i
    if a^b==x and a<=b:
     print(a,b,end='\n')
