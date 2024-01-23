# importing random module 
import random

print("Here You Can Get Your Safe Password")

# making the list of number,symbols and letters(lower and upper case)
numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ["!","@","#","$","%","^","*"]

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# asking user how many letters he/she wants in password
num_letters = int(input("How many letters do you want in your password ?\n"))

# asking user how many numbers he/she wants in password
num_numbers = int(input("how many numbers do you want in your password ?\n"))

# asking user how many symbols he/she wants in password
num_symbols = int(input("how many symbols do you want in your password ?\n"))

# creating a password list which will store password in list
pass_word = []

# creating a loop variable for implementing loop
loop = 1

l = 0 # for indexing
n = 0 # for indexing
s = 0 # for indexing

# making while loop for taking random letters
while(loop<=num_letters): # for traversing 
    l = random.randint(0,51) # for taking random letters 
    pass_word+=letters[l]
    loop+=1

loop = 1 # loop  variable like early one

# making while loop for taking random numbers
while(loop<=num_numbers): # for traversing
    n = random.randint(0,9) # for taking random number 
    pass_word+=numbers[n]
    loop+=1

loop = 1 # loop variable like early one

# making while loop for taking random symbol
while(loop<=num_symbols):# for traversing
    s = random.randint(0,6) # for taking random symbol
    pass_word+=symbols[s]
    loop+=1

# shuffling the list for random order od letters,numbers and symbols
random.shuffle(pass_word)

# converting list into char
char = ""
for i in pass_word:
    char+=i

# printing the password
print(f"Your password is {char}")
print("\n")
input("Press any key to exit.")