#Note:  A built-in data type that lets us create immutable sequences of values

tup = (2,1,3,9,6)
print(tup)
print(type(tup))        #print type of tuple

print(tup[0])           #print tuple element seperately
print(tup[1])
print(tup[2])

#tup[4] = 5             #tuple is immutable that is why value assign is not allowed

tup = ()                # empty tuple
print(tup)

#single element tuple
tup = (1,)              #correct form of single element tuple
print(tup)              
print(type(tup))        #output: tuple

tup = (1)               #Not correct form of single element tuple
print(tup)              
print(type(tup))        #output: int  || in this case python assumed 1 is a normal integer like tup = (2+4) :6