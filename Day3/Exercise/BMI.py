height = float(input("Enter your height"))
weight= float(input("Enter your weight"))
bmi = weight/(height**2)
if bmi <=18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi <=25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi<=30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")

elif bmi<=35:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi>=35:
    print(f"Your BMI is {bmi}, you are clinically obese.")
else:
    print(f"Error Your input:{bmi} is incorrect please enter valid input.")