def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest: # 3 < 5
            smallest = arr[i] # it is an element
            smallest_index = i # it is an index of this element
    return smallest_index


def selection_sort(arr): 
    new_arr = []
    for _ in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

arr = [5, 3, 2, 6, 7]
print(find_smallest(arr))
print(selection_sort(arr))
