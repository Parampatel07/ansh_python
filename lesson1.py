# Write a programe to find area of cylinder 
# A = 2πrh + 2πr2
radius = int(input("Enter raduis of cylinder "))
height = int(input("Enter height of cylinder "))

answer = (2 * 3.14159 * radius * height) + (2 * 3.14159 * (radius * radius))
print("your area of cylinder is ",answer)