#BMI = weight kg / (height)*2
weight = float(input("enter your weight:  "))
height = float(input("enter your height:  "))

86
#BMI calculation
BMI = int(weight) / float(height) ** 2

#convert 
int_bmi = int(BMI)

#print result
print(int_bmi)
