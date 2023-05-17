# Write a programe to findout whether the user given year is millinuem year or not 
# 1000,2000,3000,4000,5000....

year = int(input("Enter any year "))

if year % 1000 == 0 :
     print("it is a milliuem year ")
else :
     print("it is not a milliuem year ")
print("goodbyee...")