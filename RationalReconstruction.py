import sys
import math
from random import randrange
from utilities import *
from EffectiveThueLemma import *


def getZ(value):
	s = str(value)
	p10 = 1
	if s[0] != '0':
		p10 = 10
	for i in range(1, len(s)):
		if s[i] == '.':
			break
		p10 *= 10
	z = []
	first = int(s[0] == '0')
	for i in range(first, len(s)):
		if s[i] != '.':
			z.append(int(s[i]))
	return (p10, z)


def Theorem4_9(n, b, R):
	if R >= n:
		raise ValueError("r* >= n")
	if b < 0 or b >= n:
		raise ValueError("b < 0 or b >= n")
	r, rr = n, b	# r0, r1
	s, ss = 1, 0	# s0, s1
	t, tt = 0, 1	# t0, t1
	if r < R:
		return (r, s, t)
	if rr < R:
		return (rr, ss, tt)
	while rr != 0:
		q = r/rr
		rrr = r % rr
		r, s, t, rr, ss, tt = rr, ss, tt, rrr, (s-ss*q), (t-tt*q)
		if rr < R:
			return (rr, ss, tt)
	return None


def RationalReconstruction(value, M = int(1e9)):
	# check if value is already an integer
	if value.is_integer():
		return (value, 1)

	# get additional 10^x and z array
	p10, z = getZ(value)
	print(z)
	k = len(z)

	# 1. Compute n = 10^k and b = sum(z(i-1) * 10^(k-i)) with i = 1..k
	n = pow(10, k)
	b = 0
	for i in range(1, k+1):
		b += z[i-1] * pow(10, k-i)

	# make sure 10^k > 2(M^2)
	while M >= 10 and 2*(M**2) >= n:
		M /= 10

	# 2. Run the extended Euclidean algorithm on input n, b to obtain EEA(n, b)
	# and then apply Theorem 4.9 with n, b, and r* = t* = M to obtain the values r', s', t'.
	EEA(n, b)
	print(n, b, M)
	rr, ss, tt = Theorem4_9(n, b, M)

	# 3. Output the rational number -s'/t'
	if tt < 0:
		ss, tt = -ss, -tt
	return (-ss*p10, tt)


def main():
	if (len(sys.argv) < 2):
		return
	value = float(sys.argv[1])
	M = int(1e9)
	if len(sys.argv) > 2:
		M = int(sys.argv[2])
	p, q = RationalReconstruction(value, M)
	print("p = %ld" %(p))
	print("q = %ld" %(q))
	print("p/q = %.20lf" %(1.0*p/q))
	print("val = %.20lf" %(value))


main()