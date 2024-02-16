
## Method:  list.append()  :akta list er last element er por new arekta element add korte chaile eta use kora hoy..etake mutation o bole
list = [2,1,3]
list.append(4)
print(list)

## Method:  list.sort( )  :sorts in ascending order [1, 2, 3]
list.sort()
print(list)
fruit = ["banana", "mango", "apple"]
fruit.sort()
print(fruit)

## Method:  list.sort( reverse=True )  :sorts in descending order
list.sort(reverse=True)
print(list)

fruit.sort(reverse=True)
print(fruit)

## Method:  list.reverse( )  :reverses list 
list = [2,1,3,9,6]
list.reverse()
print(list)

fruit = ["banana", "mango", "apple"]
fruit.reverse()
print(fruit)

##  Method:  list.insert( idx, el )  :insert element at index
list = [2,1,3,9,6]
list.insert(1,99)
print(list)

##  Method:  list.remove(element)  :removes first occurrence of element
list = [2,99,3,99,9,6]
list.remove(99)       #if one element exist in a list multiple time then remove first element using this function.
print(list)

## Method:  list.pop( idx )  :removes element at idx 
list = [2,1,99,1,9,6]
list.pop(2)
print(list)