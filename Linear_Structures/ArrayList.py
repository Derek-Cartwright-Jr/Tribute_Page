""" List data structure in python is essentially a traditional arraylist 
in this file I'm just going to run some tests to go over list methods that
I may not know about or need clarifying aobut. """

def test():
	myList = []

	""" list.append(x); Adds an item to the end of the list. Equivalent to L[len(L):] = [x] """
	myList.append(23)
	print(myList)

	""" list.extend(L); Extends the list by appending all elements of another list """
	List2 = [x for x in range(10)]
	myList.extend(List2)
	print(myList)

	""" list.insert(i,x); Inserts an item x at a given position i """
	myList.insert(2, 10)
	print(myList)

	""" list.remove(x); Removes the first item from the list whose value is x """
	myList.remove(8)
	print(myList)

	""" list.pop([i]); Remove the item at the given position in the list and return it. If i
	isn't given then this becomes list.pop() and the last item is removed from the list and 
	returned """
	myList.pop(2)
	print(myList)

	""" list.clear(); Removes all items from the list """
	myList.clear()
	print(myList)

	myList = [x for x in range(10)]

	""" len(list) returns the number of items in the list """
	print(len(myList))

	""" list.index(x); Return the index in the list of the first occurence of x """
	print(myList.index(6))

	""" Return the number of times x appears in the list """
	print(myList.count(3))

	""" list.sort(); Sort the items of the list in place """
	myList.reverse()
	print(myList)
	myList.sort()
	print(myList)

	""" list.reverse(); Reverse the items of the list in place """
	myList.reverse()
	print(myList)

	""" list.copy(); Return a shallow copy of the list. Equivalent to a[:] """
	second_list = myList.copy()
	print(second_list)

	""" del statement can remove either one element or a slice of elements from a list """
	del myList[2:5]
	print(myList)
	del myList[0]
	print(myList)
	del myList[:]
	print(myList)

	""" Nested List """
	matrix = [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15]]
	print(matrix[0][2])
	print(matrix)

	""" List Compression """
	com_list = [x for x in range(0, 100, 20)]
	matrix = [[row[i] for row in matrix] for i in range(5)]
	print(com_list)
	print(matrix)

def main():
	test()

if __name__ == "__main__":
	main()