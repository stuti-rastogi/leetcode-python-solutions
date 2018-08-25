from collections import Counter
def palindromePermutation(s):
	n = len(s)
	counts = Counter(s)
	if (n % 2 == 0):
		for x in counts:
			if (counts[x] % 2 == 1):
				return False
		return True
	else:
		foundOdd = False
		for x in counts:
			if (counts[x] % 2 == 1):
				if foundOdd:
					return False
		return True

print (palindromePermutation("csdf"))
print (palindromePermutation("carerac"))