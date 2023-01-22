#for loops
fruits = ["Apple", "Pear", "Orange", "Peach", "Banana"]

for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")

#for loop - average student height
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height

average = round(total_height / (n + 1))
print(average)

#highest score 
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")
