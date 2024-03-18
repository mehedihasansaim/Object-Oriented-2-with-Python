## range() function
    
seq = range(10)
for i in seq: 
    print(i)

## 2 theke 100 porjonto all even number print 
for i in range(2, 101, 2):
    print(i) 

## 1 theke 100 porjonto all odd number print 
for i in range(1, 100, 2):
    print(i) 

## 1 theke 100 porjonto print
for i in range(1, 101):
    print(i)


## 100 theke 1 porjonto print
for i in range(100, 0, -1):
    print(i)


## Multiplication table:
n = int(input("Enter your number: "))
for i in range(1,11):
    print(n*i)