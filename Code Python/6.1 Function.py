
#function defination
def calc_sum(a,b):        #(parameters)
    sum = a+b
    print(sum)


a = 10
b = 20
calc_sum(a,b)             # function call(arguments)
calc_sum(50,40)           # function call(arguments)


## no parameter, no return value function.....

def hello():
    print("hello world")

output = hello()
print(output)           #output: None



## avg of 3 numbers......

def avg(a,b,c):
    sum = a+b+c
    avg = sum/3
    return avg

print(avg(1,2,3))       # output: 2