import random

def sequential_search(number_list, target_value):
    for i in range (len(number_list)):
        #determine if the number at the current index is equal to the target
        #if so, return the index and end the loop
        if target_value == number_list[i]:
            return i
    return -1
    
"""
Function to run binary search on a sorteded list
Inputs: list, target value
Output: found index
"""
def binary_search(arr, target_value):
    #Define the low an high indexes of the list
    low_index = 0
    high_index = len(arr) - 1 

    #Create a loop to search for target value
    while low_index <= high_index:
        #find the midpoint
        middle_index = (low_index + high_index) // 2

        #check if target value is at the middle index in the list
        if arr[middle_index] == target_value:
            return middle_index
        elif arr[middle_index] < target_value:
            low_index = middle_index + 1
        else:
            high_index = middle_index - 1
    return -1

def main():
    #create a list of 100 numbers from 1 to 100
    number_list = random.sample(range(1, 101), 100)
    number_list.sort()

    #found_index = sequential_search(number_list, 105)
    target_value = 105
    found_index = binary_search(number_list, target_value)

if found_index == -1:
    print("{target_value} not found")
else:
    print("{target_value} found at index {found_index}")

main()