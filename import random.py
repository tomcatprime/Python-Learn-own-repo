import random

#whole numbers
random_integer = random.randint(1,10)
print(random_integer)

#floating number
random_float = random.random()
print(random_float)

a = random_float * 5

print(a)

love_score = random.randint(1,100)
print(f"Your love score is {love_score}")


#list data structure

statesof_america = ["ND", "SD", "NE", "KS", "MN", "IA", "MO", "WI", "IL", "IN", "MI", "OH"]
print(statesof_america[0])
print(statesof_america[-1])
print(statesof_america)
#add item to the list
statesof_america.append("TX")

print(statesof_america)


#Who is gonna buy the meal exercise
# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
names_num = len(names)


choice = random.randint(0, names_num - 1)
buyer = names[choice]

print(f"{buyer} is going to buy the meal today!")