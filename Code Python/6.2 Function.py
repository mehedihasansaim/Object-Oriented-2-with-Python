

cities = ["Mymensingh", "Dhaka", "Rajshahi", "Barishal", "Khulna"]
marks = [12,23,34,45,56,67,78,89]

#print the length of list using function
def calc_len(list):
    print(len(list))

calc_len(cities)
calc_len(marks)

#print the list using function
def print_list(list):
    for item in list:
        print(item, end = " ")

print_list(cities)
print("\n")
print_list(marks)


### Factorial using function
print("\n")
def calc_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact*i
    print(fact)

calc_fact(5)


## check number using function

def check_num(n):
    if (n % 2 == 0):
        print("even number")
    elif(n%2 != 0):
        print("odd number")
    else:
        print("give a valid number")

check_num(22)       
check_num(23)