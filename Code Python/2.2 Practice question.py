
# #WAP to input user’s first name & print its length.
name = input("Enter your name: ")
print("Your name's length is : ", len(name))


# # WAP to find the occurrence of ‘$’ in a String.
str = "Hi, $ I am a $. $99.34"
print("Number of $ is : ",str.count("$"))


# Grade students based on marks
# marks >= 90, grade =“A”
# 90 > marks >= 80, grade =“B”
# 80 > marks >= 70, grade =“C”
# 70 > marks, grade = “D”

marks = int(input("Enter student mark: "))
if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"
print("Your grade is :", grade)