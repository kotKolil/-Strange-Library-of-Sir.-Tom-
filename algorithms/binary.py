from time import *

def BinarySearch(arr, item):
	Min = 0
	Max = len(arr) - 1
	while Min <= Max:
		mid = (Min + Max)//2
		if item == arr[mid]:
			return mid
		elif item > arr[mid]:
			Min = mid + 1
		else:
			Max = mid + 1
	return None

def SimpleSearch(arr, item):
	for i in range(0, len(arr)):
		if item == arr[i]:
			return i
	return None


t11 = time()
SimpleSearch(range(0,2**25 + 1), 2**25)
t12 = time()
print(f"Time of executing function SimpleSearch is {t12 - t11}")
t21 = time()
BinarySearch(range(0,2**25 + 1), 2**25)
t22 = time()
print(f"Time of executing function BinarySearch is {t22 - t21}")
