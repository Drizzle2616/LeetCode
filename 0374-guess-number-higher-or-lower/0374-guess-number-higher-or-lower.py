def guessNumber(self, n: int) -> int:
	low = 0
	high = n
	while low <= high:
		mid = (low + high ) // 2
		res = guess(mid)
		if res < 0:
			high = mid - 1

		elif res > 0:
			low = mid + 1

		else:
			return mid