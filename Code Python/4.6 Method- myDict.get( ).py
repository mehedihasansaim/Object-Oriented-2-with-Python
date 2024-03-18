

#return the key according to value
info = {
    "key" : "value",
    "name" : "mehedi hasan saim",
    "learning" : "coding",
    "age" : 35,
}

# value access korar 2 way ace...(1)Normar way (2)Using .get() function
print(info.get("name"))            #Using .get() function
print(info["name"])                #Normal way


# Difference between two method:
# name2 key is not available in our dictionary
print(info.get("name2"))      # No Error -> None
print(info["name2"])          # Error      
