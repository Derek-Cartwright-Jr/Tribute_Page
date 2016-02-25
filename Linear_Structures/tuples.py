""" Tuples consists of a number of values seperated by commas """

def test():
	t = 12345, 54321, 'Hello'
	print(t)

	""" Tuplex may be nested """
	new_t = t, 5, 6, 7, 8, 9, 10
	print(new_t)

	""" Tuples can be indexed """
	print(t[0])

	""" Note: Tuples Are Immutable! So you can't do item assignment """

def main():
	test()

if __name__ == "__main__":
	main()
