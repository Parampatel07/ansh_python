# Write a programe to findout wether the user is eligible for voting or not if yes then ask for input m = male and f = female also check wether the size of input is 1 or greater if greater show invalid input 

age = int(input("Enter your age "))
vote = 0 
vote_bank = {'male':0,'female':0}
if age >= 18:
     print("you are eligible for voting ")
     print("Please Select One of Below ")
     print("Press M to vote for Male and F to vote for Female ")
     vote = input("")
     if len(vote) == 1 :
          if vote == 'M' or vote == 'm':
               vote_bank['male'] += 1
          elif vote == 'F' or vote == 'f' :
               vote_bank['female'] += 1
     if vote_bank['male'] > vote_bank['female']:
          print("Male Has Been Selected ")
     elif vote_bank['male'] < vote_bank['female']:
          print("Female Has Been Selected ")
     else:
          print("Result is Not Satisfied ")
else:
     print("You cannot vote ")
