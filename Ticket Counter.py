print("Welcome to the tollercoaster!")
height  = int(input("What is your height in cm?"))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age <12:
        bill =5
        print("Child tickets are $5.")
    elif age <= 18:
        print("Youth tickets are $7.")
        bill = 7
    else:
        print("Adult tickers are $12.")
        bill =12

    wants_photo = input("Do you want a photo takne? Y or N. ")
    if wants_photo == "Y":
        #add $3 to thei bill
        bill += 3
    print (f"Your final bill is {bill}")
else:
    print("Sorry, you have to griw taller before you can ride.")