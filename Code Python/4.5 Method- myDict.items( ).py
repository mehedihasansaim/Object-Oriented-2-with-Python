

##returns all (key, val) pairs as tuples
student ={
    "name" : "Mehedi Hasan Saim",
    "subjects" : {
        "physics" : 97,
        "chemistry" : 95,
        "math" : 90
    }
}

print(student.items())

#print using list
print(list(student.items()))

#Access individual pairs or items
pairs = list(student.items())
print(pairs[0])
print(pairs[1])