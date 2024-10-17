def remove_duplicates(input_list):
    unique_list = []
    
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
 
    return unique_list

def sort_list(cleaned_list):
    numbers = []
    strings = []

    for item in cleaned_list:
        if type(item) == int:
            numbers.append(item)
        elif type(item) == str:
            strings.append(item)
    
    numbers.sort()
    
    strings.sort(key=str.lower)
    
    return numbers + strings

input_list = [3, 1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 'Привіт', 'анаконда']

unique_list = remove_duplicates(input_list)

sorted_list = sort_list(unique_list)

print(sorted_list)
