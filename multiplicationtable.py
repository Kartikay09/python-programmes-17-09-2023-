#multiplication table 
n=int(input("enter your number for which you want multiplication table: "))
a = 0
b = 1
s = 0
count = 1

while count!=11:
    print(n," * ", count ," = ",count*n)
    count +=1
    
