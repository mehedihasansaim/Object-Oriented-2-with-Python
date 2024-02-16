

str1 = "This is a string"
str2 = 'This is a string'
str3 = '''This is a string'''
str4 = """This is a string"""
print(type(str4))

#newline
str5 = "This is \nMehedi Hasan Saim"
print(str5)

#String Operation---------------

#string concatination
s1 = "Mehedi Hasan"
s2 = " Saim"
final_name = s1 + s2
print(final_name)

#length of string 
length1 = len(s1)
length2 = len(s2)
length3 = len(final_name)
print(length1)
print(length2)
print(length3)

#Indexing
str6 = "Mehedi Hasan Saim"
ch1 = str6[0]
ch2 = str6[1]
ch3 = str6[2]
ch4 = str6[3]
print(ch1)
print(ch2)
print(ch3)
print(ch4)
print(str6[4])

#slicing
str7 = "MehediHasan"
slicing = str7[1:4] # 1,2,3 number index print korbe
print(slicing)         #str7[:4] means start theke 3 porjonto print korbe
                       #str7[1:] && str7[1:len(str7)] means 1 theke ses porjonto print korbe



### String function:

#endswith()
str8 = "I am studying in Apnacollege"
# string ta kon word diye ses hosse seta check kora jay endswith() fucntion diye. 
print(str8.endswith("ege"))  #true
print(str8.endswith("app"))  #false

#capitalize()
str9 = "i am studying in Apnacollege"