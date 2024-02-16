##  WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)

list1 = [1,2,3,2,1]
list2 = [1,2,3,4]

copy_list1 = list1.copy()
copy_list1.reverse()
if(copy_list1 == list1):
    print("List 1 is Palindrome")
else:
    print("List 1 is Not palindrome")

copy_list2 = list2.copy()
copy_list2.reverse()
if(copy_list2 == list2):
    print("List 2 is palindrome")
else:
    print("List 2 is not palindrome.")


list3 = ['m', 'a', 'a', 'm']
copy_list3 = list3.copy()
copy_list3.reverse()
if(copy_list3 == list3):
     print("List 3 is palindrome")
else:
    print("List 3 is not palindrome.")
