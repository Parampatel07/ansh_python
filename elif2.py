# 10) Write a Python program to calculate final electricity bill based upon below given criteria. take monthly electricity unit from user as input. 

# units           price  per unit 
# <100            1
# >100 & <200     2 
# >200 & <300     3
# >300 & <400     4
# >400            5

# also calculate 5% percentage energy charge on total bill amount & display total amount 

unit =int(input("Enter number of electricity unit "))
price = 0

if unit < 100:
     price = 1
elif unit >= 100 and unit < 200:
     price = 2
elif unit >= 200 and unit < 300:
     price = 3
elif unit >= 300 and unit < 400:
     price = 4
elif unit >= 400:
     price = 5

total_bill = unit * price

energy_charge = total_bill * 5 / 100

total_bill += energy_charge
print("your total bill is ",total_bill)