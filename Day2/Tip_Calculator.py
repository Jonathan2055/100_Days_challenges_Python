# Details About this app
#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
Total_Bill=float(input("What was the total bill?  $"))
Tip=int(input("How much tip would you like to give? 10, 12, or 15? "))
Contributors= int(input("How many people to split the bill?"))
Each_Contributor=round((Total_Bill+Total_Bill*Tip/100)/Contributors,2)
print(f"Each person should pay: ${Each_Contributor}")