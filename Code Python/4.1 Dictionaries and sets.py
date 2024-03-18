info = {
    "key" : "value",
    "name" : "mehedi hasan saim",
    "learning" : "coding",
    "age" : 35,
    "is_adult" : True
}
print(info)

# add list and touple in dictionary
dict ={
    "name" : "mehedi",
    "subject" : ["bangla", "English", "Math"],    #list
    "topics" : ("first", "second")                #touple
}
print(dict)

## How to access or print information inside dictionary 
print(info["name"])
print(dict["name"])
print(dict["subject"])

# Existing key value change and new value assign
# jodi ami info dictionary er name change korte chai....
info["name"] = "Mehedi Hasan"
# new value assign korte chaile...
info["surename"] = "Saim"
print(info)