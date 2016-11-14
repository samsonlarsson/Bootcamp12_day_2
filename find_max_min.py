def find_max_min(A):
	minimum = min(A) 
	maximum = max(A)

	if minimum == maximum:
		return [len(A)] # if min no. equals max no., length of string is returned 
	return [minimum, maximum]