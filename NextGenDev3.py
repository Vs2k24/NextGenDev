#task 3 to create a password generator 
import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','&','(',')','*','+']
print("welcome to password generator app")
#now ask the user how many numbers you want how many symbols you want etc 
n_letters=int(input("how many letters you want in your password: "))
n_numbers=int(input("how many numbers you want in your password: "))
n_symbols=int(input("how many symbols you want in your password: "))
#now we need to generate letters symbols and numbers from the list we can take a empty list and add whatever we want
password_list=[]
#if u want to generate 4 letters you need to use a for loop
for i in range(1,n_letters+1):
    char=random.choice(letters)#in brackets pass the list name
    #update password_list
    password_list+=char
#now create a for loop for all then update password_list
for i in range(1,n_symbols+1):
    char=random.choice(symbols)
    password_list+=char
for i in range(1,n_numbers+1):
    char=random.choice(numbers)
    password_list+=char
print(password_list)
#now shuffle this list 
random.shuffle(password_list)
print(password_list)
#we need the password in the form of a string 
#take an empty string 
password=""
for char in password_list:
    password+=char
print(password)