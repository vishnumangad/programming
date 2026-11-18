import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers=[0,1,2,3,4,5,6,7,8,9]
spechar=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', ';', ':', ',', '.', '<', '>', '/', '?']
noletters=int(input("How many letters would you like in your password?\n"))
nonumbers=int(input("How many numbers would you like in your password?\n"))
nospechar=int(input("How many special characters would you like in your password?\n"))
password=""
for i in range(noletters):
    password+=random.choice(letters)
for i in range(nonumbers):
    password+=str(random.choice(numbers))
for i in range(nospechar):
    password+=random.choice(spechar)
print("Your generated password is:", password)