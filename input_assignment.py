#WAP to take user input email and validate wether it is correct email or not
email = input("Enter your email address: ")

if "@" in email and ".com" in email:
    print("Its valid email")
else:
    print("Its not valid input")
    
#WAP to take user input mark percentage and find their division.

percentage = int(input("Enter your percentage: "))

if percentage >= 80 and percentage <= 100:
    print(f"First Division and your percentage is {percentage}%")
elif percentage >= 60 and percentage < 80:
    print(f"Second Division and your percentage is {percentage}%")
elif percentage >= 40 and percentage < 60:
    print(f"Third Division and your percentage is {percentage}%")
elif percentage > 100:
    print("Please enter upto 100 only")
else:
    print("Fail")