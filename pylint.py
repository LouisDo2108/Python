def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True
    
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
                    
    return arr

a = [1, 87, 2, 4, 7, 6, 3, 5, 8]

try: 
    array = [int(d) for d in a]
    array = bubble_sort(a)
except:
    print("Your list probably has one or more non int variables")
    print("Your list is unsortable!")
else:
    print("Here is your sorted list: {}".format(array))
finally:
    print("You have done a bubble sort")
    