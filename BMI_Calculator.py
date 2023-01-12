#BMI = weight kg / (height)*2
weight = float(input("enter your weight:  "))
height = float(input("enter your height:  "))


#BMI calculation based on input
BMI = int(weight) / float(height) ** 2

#convert 
int_bmi = int(BMI)

#print result
print(int_bmi)

#if-else
if int_bmi >= 50:
    print("you BMI is Obesity")
else:
    print(f"Your BMI {int_bmi} is in good condition")