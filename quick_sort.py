#Quicksort Algorithm

def quicksort(arr):
    
    #if array has one item. return list because it is already sorted
    if len(arr) <= 1:
        return arr
    
    stack = []
    stack.append((0, len(arr)-1))

    while len(stack) > 0:
        pass

def main():
    arr = [50, 30, 80, 20, 10, 70, 60]
    quicksort(arr)

main()