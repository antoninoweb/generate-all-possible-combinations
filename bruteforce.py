# @description: generate all possible characters & combinations of a given string without using libraries
# @syntax:
# generate(string_to_array("abcdef"), 4)
# generate(['a', 'b', 'c'], 2)

def generate(chars, pos, combinations = []):

	if len(combinations) == 0:
		combinations = chars

	if pos == 1:
		return combinations

	result_combinations = []

	for combination in combinations:
		print(combination)
		for char in chars:
			result_combinations.append(combination + char)

	array_print(result_combinations)

	return generate(chars, pos-1, result_combinations)

def array_print(input):
	for item in input:
		print(item)
	return

def string_to_array(string):
	chars = []
	for char in string:
		chars.append(char)
	return chars

chars = "abcdefghijklmnopqrstuvwxyz"
generate(string_to_array(chars), 2)
