def quick_sort(arr):
	# base case of recursion 
	if len(arr) <= 1:
		return arr
	# support element (pivot)
	pivot = arr[0]
	# find less el than pivot, and bigger elements than pivot
	left_less = list(filter(lambda x: x<pivot, arr))
	center = [i for i in arr if i == pivot]
	right_more = list(filter(lambda x: x >pivot, arr))

	return quick_sort(left_less) + center + quick_sort(right_more)

print(quick_sort([7, 6, 10, 5, 9, 8, 3, 4]))