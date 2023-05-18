# 12) Write a program to display zodiac symbol & given zodiac sign from given birth day and month as per following criteria.
# https://in.pinterest.com/pin/81698180718875314/

month = int(input("Enter your birth month "))
day = int(input("Emter your birth day "))
# zodiac_sign = 0
if (month == 3 and day >= 21) or (month == 4 and day <= 19):
     print("your sign is aries ")