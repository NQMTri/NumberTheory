import sys
import math
from random import randrange
from utilities import *
from EffectiveThueLemma import *


# p is prime
def findBeta(p):
	beta = 0
	p4 = (p-1)/4
	while mpow(beta, 2, p) != p-1:
		x = randrange(0, p)
		beta = mpow(x, p4, p)
	return beta


# input: p is a prime that has form 4k+1.
# output: two integers r and t such that r^2 + t^2 == p.
def Fermat2Squares(p):
	# if not isPrime(p):
	# 	raise ValueError("%ld is not prime." % (p))
	if mmod(p, 4) != 1:
		raise ValueError("%ld does not have form 4k+1.")
	beta = findBeta(p)
	b = mmod(beta, p)
	eea = EEA(p, b)
	return EffectiveThueLemma(p, b, math.floor(p**0.5)+1)


def main():
	if (len(sys.argv) < 2):
		return
	p = int(sys.argv[1])
	r, t = Fermat2Squares(p)
	print("p = %ld" %(p))
	print("r, t = %ld, %ld" %(r, t))
	print("r^2 + t^2 == p is %s" %(r**2 + t**2 == p))


main()