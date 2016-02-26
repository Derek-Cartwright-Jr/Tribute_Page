""" Binary Search """

def binary_search(arr, item):
	arr.sort()
	first = 0
	last = len(arr)
	found = False

	while first<=last and not found:
		middle = (first+last)//2
		if arr[middle] == item:
			found = True
		else:
			if item < arr[middle]:
				last = middle-1
			else:
				first = middle+1
	if found:
		return found, arr.index(item)
	else:
		return found

""" Running some tests """
def test():
	print(binary_search([1, 2, 3, 45, 84, 100], 100))
	print(binary_search([54, 23, 12, 100, 93, 82, 73, 1, 43, 22, 76], 12))
	print(binary_search([12, 43, 54, 65, 1, 2, 57, 90, 43, 22], 65))

def main():
	test()

if __name__ == "__main__":
	main()