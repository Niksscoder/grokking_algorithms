
def find_max(arr):
    if len(arr) == 2:
    	if arr[0] > arr[1]:
    		return arr[0]
    	else:
        	return arr[1]
    sub_max = find_max(arr[1:])
    if arr[0] > sub_max:
    	return arr[0]
    else:
    	return sub_max


print(find_max([11, 10,3,4,20]))