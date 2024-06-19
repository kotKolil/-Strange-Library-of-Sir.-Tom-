def selection_sort(arr:list):
	arr2 = []
	while len(arr) != 0:
		arr2.append(max(arr))
		arr.remove(max(arr))

	return arr2

print(selection_sort(list(range(1,100+1))))