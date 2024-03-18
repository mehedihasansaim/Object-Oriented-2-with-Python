

collection = set() #empty set

#set.add(el):
collection.add(1)
collection.add(2)
collection.add(2)

print(collection)   #output: 

#set.remove(el):
collection.remove(1)

print("After removing element new set :\n",collection)
print("\n")
collection.add("hello")
collection.add((1,2,3,4))                # set er modde touple add 
print(collection)            
print("length of collection before clear the set:")
print(len(collection))      #output: 3

collection.clear()
print("length of collection after clear the set:")
print(len(collection))      #output: 0


#set.pop(): 
set = {"mehedi", "hasan", "saim", "hello", "world"}
set.pop()          #removed
print(set.pop())   #removed

print(set)         #output: removed two value


### set.union():

set1 = {1,2,3}
set2 = {3,4,5}
print(set1.union(set2))  #output: {1,2,3,4,5}


### set.intersection():

set1 = {1,2,3}
set2 = {2,3,4,5}
print(set1.intersection(set2))  #output: {2,3}

