# # 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# # 🚨 Don't change the code above 👆
#
# ####################################
# #Write your code below this line 👇
#
# first_digit=int(two_digit_number[0])
# second_digit=int(two_digit_number[1])
# sum_of_digits=first_digit+second_digit
# print(sum_of_digits)
#
#
#
#
#
def to_camel_case(text):
    i = 0
    my_text = ""
    # Check each char
    for char in text:
        if text[i - 1] == "-" or text[i - 1] == "_":
            my_text += text[i].upper()
            
        else:
            my_text += char
        my_text=my_text.replace('_','')
        my_text=my_text.replace('-','')
        i = i + 1
    print(my_text)


to_camel_case("Joe_mugisha")