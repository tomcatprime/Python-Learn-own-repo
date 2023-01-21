#miles to KM

# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return km
my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the conversion
print(f"The distance in kilometers is {my_trip_km} ")

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
doubling = my_trip_km * 2
print(f"The round-trip in kilometers is {doubling} ")

#comparing two number
# This function compares two numbers and returns them in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)

#fractional part function
def fractional_part(numerator, denominator):
	# Operate with numerator and denominator to 

	if denominator:
		res = numerator/denominator
	else:
		res = 0
	res = res - int(res)
# keep just the fractional part of the quotient
	return res

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0
