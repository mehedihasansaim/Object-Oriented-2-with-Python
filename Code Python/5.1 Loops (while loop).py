
count = 1
while count <=5: 
    print("Hello world")
    count += 1

#Print number from 1 to 100
print("Print number 1 to 100: ")
i = 1
while i<=100:
    print(i)
    i +=1

#print number from 100 to 1
print("Print number 100 to 1: ")
j = 100
while j>=1:
    print(j)
    j-=1

# Print the multiplication table of a number n.
print("Multiplication table: ")
k = 1
while k <= 10:
    print(k*3)
    k += 1


# Print the elements of the following list using a loop: [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
num = [1,2,3,4,5,6,7,8,9]
idx = 0
while idx < len(num):
    print(num[idx])
    idx += 1

#Search for a number x in this tuple using loop:[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
x = 36
l = 0
while l < len(numbers):
    if(numbers[l] == x):
        print("Value found at idx ",l)
    l += 1