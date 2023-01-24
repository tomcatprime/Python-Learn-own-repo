import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#easy level - add characters, letters and numbers
password = ""
for char in range(1, nr_letters + 1):
    random_char = random.choice(letters)
    password = password + random_char
#or 1 line password += random.choice(letters)
for sym in range(1, nr_symbols + 1):
    random_sym = random.choice(numbers)
    password = password + random_sym
#or 1 line password += random.choice(numbers)]
for num in range(1, nr_numbers):
    password +=  random.choice(symbols)
print(f" Your password is:  {password}")


#randomize characters from list
password1 = []
for char in range(1, nr_letters + 1):
    password1.append(random.choice(letters))
#or 1 line password += random.choice(letters)
for sym in range(1, nr_symbols + 1):
    password1.append(random.choice(symbols))
#or 1 line password += random.choice(numbers)]
for num in range(1, nr_numbers):
    password1.append(random.choice(numbers))
random.shuffle(password1)
pass2 = ""
for char1 in password1:
    pass2+= char1
print("-----------or-----------")
print(f"Your Password is:  {pass2}")