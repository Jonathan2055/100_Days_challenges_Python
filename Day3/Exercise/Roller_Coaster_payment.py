print("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm?"))
if height>=120:
    print("You can ride the rollercoaster")
    age=int(input("What is ur age?"))
    if age<12:
        print("Child tickets are $5. ")
    elif age<=18:
        print("Youth tickets are $7.")
    elif age>=45 and age<=55:
        print("You can ride for free.")

    else:
        print("Adult tickets are $12.")
else:
    print("Sorry, you have to grow taller before you can ride")