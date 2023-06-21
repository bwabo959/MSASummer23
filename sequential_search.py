import random

def sequential_search(number_list, target_value):
    for i in range (len(number_list)):
        #determine if the number at the current index is equal to the target
        #if so, return the index and end the loop
        if target_value == number_list[i]:
            return i
    return -1
    

def main():
    #create a list of 100 numbers from 1 to 100
    number_list = random.sample(range(1, 101), 100)
    number_list.sort()

    found_index = sequential_search(number_list, 105)

    print(found_index)

main()