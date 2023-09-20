#sum of even number using while loop
import random
rndm = random.randint(0,100)
n = int(input("enter limit : "))
sum = 0
i = 0

while i<=n:
    sum += i
    i +=2
print("sum of even numbers upto ",n," is ",sum)
    
    
