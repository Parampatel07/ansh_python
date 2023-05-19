# Write a programe to findout how many days a month has without using and or elif 

month = int(input("Enter any month "))

if month <= 12:
     if month >= 1:
          if month <= 7:
               if month == 2 :
                    print("it has 28 - 29 days ")
               else:
                    if month % 2 == 0:
                         print("it has 30 days ") 
                    else:
                         print("it has 31 days ")
          else:
               if month % 2 == 0 :
                    print("it has 31 days ")
               else:
                    print("it has 30 days ")
     else:
          print("invalid input ")
else:
     print("invalid input ")