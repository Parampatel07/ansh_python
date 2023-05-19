# Write a programe to findout largest number outof given three numbers 
num1 = int(input("Enter value of num1 "))
num2 = int(input("Enter value of num2 "))
num3 = int(input("Enter value of num3 "))

if num1 == num2 and num2 == num3:
     print("All are same ")
else:
     if num1 > num2 :
          if num1 > num3 :
               print("num1 is largest ")
          else :
               print("num3 is largest ")
     else:
          if num2 > num3 :
               print("num2 is largest ")
          else :
               print("num3 is largest ")
print("Goodbyee...")