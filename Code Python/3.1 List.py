#List = [1,2,3,4,5]
#tuple = (1,2,3,4,5)

### List
marks = [85.2, 12.9, 33.5, 61.4, 55, 74]
print(marks)
print(type(marks))

#print value according their index
print(marks[0])
print(marks[4])

# length of list
print(len(marks))

#Note: c++ ,c asob language e array er vitoe ak e type er data store kora jay , different type er data store kora jay na...bt python e list e amra multiple type er data ak e list er vitore store korte pari....
person = ["saim", 85.5, 12, "bangladesh"]

#    String = immutable = change kora jay na = index e value ke access kora jay bt value change kora jay na.. 
str = "Saim"
print(str[0])
#str[0] = "mehedi", when we try to access the str[0] value then we face a error...

#    list = mutable = change kora jay = index e value ke access o kora jay and value change o kora jay..
list = ["saim", 12.4, "dhaka"]
print(list[0])
list[0] = "mehedi"
print(list)
