#Palindrome check
n = int(input("Enter the number: "))
m = n
ans = 0
i = 0

while n!=0:
    s = n%10
    ans = ans*10 + s
    i = i+1
    n = n//10
if m == ans:
    print("entered number is Palinderome")
else:
    print("entered number is not Palinderome")
    
