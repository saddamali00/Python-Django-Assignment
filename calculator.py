# write a calculator programme

fNumber = int(input("first number: "))
op = input("enter operator (+,-,*,/,%): ")
sNumber = int(input("second number: "))

if op == "+":
    print(f"your sum is: {fNumber+sNumber}")
elif op == "-":
    print(f"your sum is: {fNumber-sNumber}")
elif op == "*":
    print(f"your sum is: {fNumber*sNumber}")
elif op == "/":
    print(f"your sum is: {fNumber/sNumber}")
elif op == "%":
    print(f"your sum is: {fNumber%sNumber}")
else:
    print("Please input correct operator 😊")


num = int(input("Enter the number: "))
if num % 2 == 0 or num % 3 == 0:
    print("composite number")
else:
    print("Prime number")
    
