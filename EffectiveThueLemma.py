from utilities import *
from EEA import EEA


def EffectiveThueLemma(n, b, R):
	if n < R:
		raise ValueError("n < r*")
	if b < 0 or b >= n:
		raise ValueError("b < 0 or b >= n")
	r, rr = n, b	# r0, r1
	s, ss = 1, 0	# s0, s1
	t, tt = 0, 1	# t0, t1
	if r < R:
		return (r, t)
	if rr < R:
		return (rr, tt)
	while rr != 0:
		q = r/rr
		rrr = r % rr
		r, s, t, rr, ss, tt = rr, ss, tt, rrr, (s-ss*q), (t-tt*q)
		if rr < R:
			return (rr, tt)
	return None


def check(n, b, R):
	T = n / R + 1
	while R*T <= max(n, R):
		T += 1
	print("n = %ld" %(n))
	print("b = %ld" %(b))
	print("r* = %ld" %(R))
	print("t* = %ld" %(T))
	print("-------------------------------------------------")
	ans = EffectiveThueLemma(n, b, R)
	r, t = ans
	print("EEA: (d, s, t) = (%ld, %ld, %ld)" % EEA(n, b))
	print("r = %ld" %(r))
	print("t = %ld" %(t))
	print("-------------------------------------------------")
	tmp1 = mmod(r, n)
	tmp2 = mmod(b*t, n)
	print("r = bt (mod n):    %ld = %ld is %s" %(tmp1, tmp2, tmp1 == tmp2))
	print("0 <= r < R:    0 <= %ld < %ld is %s" %(r, R, r < R))
	print("0 < |t| < T:    0 <= %ld < %ld is %s" %(abs(t), T, abs(t) < T))


# check(10, 7, 3)
# check(1234567891011121314151617, 9876543210, 29)