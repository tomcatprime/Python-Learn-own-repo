values = [23, 52, 59, 37, 48]
sum = 0
lenght = 0
for value in values:
    sum += value
    lenght += 1
print(str(sum))
print(str(lenght))
print(sum + lenght)

product = 1
for n in range(1,10):
    product = product * n
print(product)

#
def to_celcius(x):
    return (x-32)*5/9

for x in range(0,101,10):
    print(x, to_celcius(x))


for left in range(7):
    for right in range(left,7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()

#all possible team pairing
teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_teams in teams:
        if home_team != away_teams:
            print(f"{home_team} vs {away_teams}")


#all possible fruit pairing
fruits = ['apple', 'pear', 'banana', 'orange']
for pair1 in fruits:
    for pair2 in fruits:
        if pair1 != pair2:
            print("-----------------------------------------")
            print(f"You're pie will contain {pair1} and {pair2}")



#recursive
def is_power_of(number, base):
  # Base case: when number is smaller than base.
  number = number/base
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return False
  else:
    return True

  # Recursive case: keep dividing number by base.
  return is_power_of(number,base)



print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False



#Implement the sum_positive_numbers function, as a recursive function that returns the sum of all positive numbers between the number n received and 1. For example, when n is 3 it should return 1+2+3=6, and when n is 5 it should return 1+2+3+4+5=15.


def sum_positive_numbers(n):
  if n <= 1:
    return n
  return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15


# The counter function counts down from start to stop when start is bigger than stop, and counts up from start to stop otherwise. Fill in the blanks to make this work correctly.
def counter(start, stop):
	x = start
	if start > stop:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			if x > stop:
				return_string += ","
			x -= 1
	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			if x < stop:
				return_string += ","
			x += 1
	return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"

#The even_numbers function returns a space-separated string of all positive numbers that are divisible by 2, up to and including the maximum that's passed into the function. For example, even_numbers(6) returns “2 4 6”. Fill in the blank to make this work.

def even_numbers(maximum):
	return_string = ""
	for x in range(2, maximum+1, 2):
		return_string += str(x) + " "
	return return_string.strip()

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed

for x in range(1, 10, 3):
    print(x)