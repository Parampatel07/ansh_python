# Write a programe to peform swap 
# a = 10 , b = 200
# a = 200 , b = 10 

a = float(input("Enter num1 "))
b = float(input("Enter num2 "))
print(f"the value of a before swap is {a} and b before swap is {b} ")
a = a + b
b = a - b
a = a - b
print(f"the value of a after swap is {a} and b after swap is {b} ")