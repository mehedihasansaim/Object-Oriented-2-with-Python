## WAP to find the sum of first n numbers. (using while)

n = int(input("enter the value of n: "))
sum = 0
for i in range(n+1):
    sum += i
print(sum)

##  WAP to find the factorial of first n numbers. (using for)
n=5
fact = 1
i = 1
while i<= n:
    fact *= i
    i +=1
print("factorial = ", fact)