""" Insertion Sort """

def insertion_sort(arr):
	for ind in range(1, len(arr)):

		currentvalue = arr[ind]
		position = ind

		while position>0 and arr[position-1]>currentvalue:
			arr[position] = arr[position-1]
			position = position-1

		arr[position] = currentvalue

def test():
	array = [199, 23, 52, 12, 90, 44, 6, 100]
	(insertion_sort(array))
	print(array)

def main():
	test()

if __name__ == "__main__":
	main()