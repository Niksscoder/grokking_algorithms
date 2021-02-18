# Find the bigger value in an array

def find_bigger(arr):
    bigger = arr[0]
    bigger_index = 0
    for i in range(1, len(arr)):
        if arr[i] > bigger: # 3 < 5
            bigger = arr[i] # it is an element
            bigger_index = i # it is an index of this element
    return bigger_index


# sort array 
def selection_sort(arr): 
    new_arr = []
    for _ in range(len(arr)):
        # Find tha bigger element in the array and add is to the new array 
        bigger = find_bigger(arr)
        new_arr.append(arr.pop(bigger)) # pop(index of element)
    return new_arr

arr = [5, 3, 2, 6, 7]
print(find_bigger(arr))
print(selection_sort(arr))
