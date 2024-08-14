import random

# --------------------------------WHILE LOOP--------------------------------

# -------------INCREMENT---------------
count = 0
while count <= 10:
    print(count)
    count += 1
    


# -------------DECREMENT---------------
count1 = 10
while count1 >= 0:
    print(count1)
    count1 -= 1
    
    

# -------------USING RANGE---------------
i = 0
while i in range(5):
    print(i)
    i+=1
    


num = 1

while num <= 50:
    if num % 2 == 0:
        print("even ", num)
    else:
        print("odd ",num)
    num +=1


# ======== ASSIGNMENT =========
random_number = random.randint(1, 50)

count = 1

while count <= 5:
    gues_number = int(input('Enter the gues numer: '))
    if gues_number == random_number:
        print("Congratulation you guess is correct 😊")
        break
    else:
        print("Try Again")
    count += 1
    