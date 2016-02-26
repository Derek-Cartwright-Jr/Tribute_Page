def sequential_search(arr, item):
	pos = 0
	found = False

	while pos < len(arr) and not found:
		if arr[pos] == item:
			found = True
		else:
			pos += 1

	return found
