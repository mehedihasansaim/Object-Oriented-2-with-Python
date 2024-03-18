
#print list using for loop
nums = [2,3,4,6,8,9]
for val in nums:
    print(val)

#print tuple using for loop
print("\nStart tuple")
tup = (2,3,4,5,6,7)
for val in tup :
    print(val)

#print character of a string
print("start string here: ")
str = "Mehedi Hasan saim"
for ch in str:
    print(ch)

#search a character in a string 
print("Searching start here : ")
str1 = "MehediHasanSaim"
for ch in str1:
    if(ch == 'H'):
        print("H is found")
        break
    print(ch)
else:                    #python e for er por akta else use kora jay...na korlew kono problem nai..for loop e break er por else execute kore na...bt jodi for er por else use kora chara kono line likhi seta default exicute hobe, break er porew kaj korbe..
    print("end")


#withour using else ...in this case after break statement print("end") will exicute.
str1 = "MehediHasanSaim"
for ch in str1:
    if(ch == 'H'):
        print("H is found")
        break
    print(ch)                   
print("end")


#Search for a number x in this tuple using loop:[1, 4, 9, 16, 25, 36, 49, 64, 81,100]

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
x = 64
idx = 0
for val in nums:
    if(val == x):
        print("value is found at index ", idx)
        break
    idx +=1