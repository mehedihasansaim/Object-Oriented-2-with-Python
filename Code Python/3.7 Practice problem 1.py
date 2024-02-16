## WAP to ask the user to enter names of their 3 favorite movies & store them in a list.

list = []
print(type(list))
print("Enter your 3 favorite movie name: ")
mov1 = input()
mov2 = input()
mov3 = input()

list.append(mov1)
list.append(mov2)
list.append(mov3)
print(list)

#another way to solve
list = []
movies = input("enter first movie: ")
list.append(movies)

movies = input("enter second movie: ")
list.append(movies)

movies = input("enter third movie: ")
list.append(movies)
print(list)

#another way to direct solve
list = []
list.append(input("enter first movie: "))
list.append(input("enter second movie: "))
list.append(input("enter third movie: "))

print(list)