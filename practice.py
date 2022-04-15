list_of_arrays = [[1,2,3],[4,6,7],[5,7,9]]
list_of_numbers = []

for array in list_of_arrays:
    for num in array:
        list_of_numbers.append(num)
        
print(list_of_numbers)