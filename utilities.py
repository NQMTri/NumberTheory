import math


def mmod(a, n):
	ans = a % n
	if (ans < 0):
		return ans + n
	return ans


def isPrime(n):
	if n < 2:
		return False
	for i in range(2, n):
		t = i*i
		if t > n:
			break
		if (n%i) == 0:
			return False
	return True