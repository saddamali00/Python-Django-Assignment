data = "123456"

sum = 0

for i in data:
    sum += int(i)
    
print(sum)


#=========================HIGHEST NUMBER ===========================

data = "789120345"

highest_number = 0

for digit in data:
    if int(digit) > highest_number:
        highest_number = int(digit)

print("Highest number:", highest_number)



#=========================LOWEST NUMBER ===========================
data = "978434521064523528"

lowest_number = int(data[0])

for i in data:
    if int(i) < lowest_number:
        lowest_number = int(i)
        
print("Lowest number is: ", lowest_number)
