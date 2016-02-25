inp = """a3, 4, b4, 5, c6
a4, 2, b6, 19, c7"""

inp2 = """"San Francisco, CA", 800000
"San Diego, CA", 800000
"Pheonix, AZ", 800000
"""

def parse(input):
	rows = input.split('\n')
	result = []
	for row in rows:
		result.append(row.split(','))

	return result

print(parse(inp2))