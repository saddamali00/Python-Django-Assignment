list_data = [1,5,9,0,6,89,1203,4,23]

for i in range(0, len(list_data)):
    
    for j in range(i, len(list_data)):
        
        if list_data[i] >= list_data[j]:
            list_data[i],list_data[j] = list_data[j], list_data[i]
            
print(list_data)


