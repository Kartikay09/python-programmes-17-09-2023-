#guess the number
import random
crt_pswrd = random.randint(10000000,100000000)

your_pswrd = int(input("enter your guess : "))
print("computer random password is ",crt_pswrd)
while crt_pswrd!=your_pswrd:
    print("your entered password is not correct")
    your_pswrd=int(input("enter your guess again: "))
else:
    print("#####your entered password is right#####")
    
