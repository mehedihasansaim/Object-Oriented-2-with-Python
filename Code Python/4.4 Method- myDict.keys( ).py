info = {
    "key" : "value",
    "name" : "mehedi hasan saim",
    "learning" : "coding",
    "age" : 35,
}

student ={
    "name" : "Mehedi Hasan Saim",
    "subjects" : {
        "physics" : 97,
        "chemistry" : 95,
        "math" : 90
    }
}

print(info.keys())
print(student.keys())

# key gula jodi list akare print korte chai tahole list type e type custing korte hobe...
print(list(info.keys()))
print(list(student.keys()))

# length of dictionary key
# without list
print(len(info.keys()))
print(len(student.keys()))

# with list
print(len(list(info.keys())))
print(len(list(student.keys())))
