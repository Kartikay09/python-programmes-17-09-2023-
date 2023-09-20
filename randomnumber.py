#guess the number
import random
rndm = random.randint(0,100)
n = int(input("enter your guess : "))

while n!=rndm:
    print("computer random number is ",rndm)
    print("your guess is not correct")
    n=int(input("enter your guess again: "))
else:
    print("#####your guess is right#####")
    
