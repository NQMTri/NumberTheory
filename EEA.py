from utilities import *


# input: two integers a, b
# output: three integers d, s, t such that
#       d = gcd(a, b)
#   and a*s + b*t = 1
def EEA(a, b):
    print("EEA(%ld, %ld):" %(a, b))
    printEntry("i", "r(i)", "q(i)", "s(i)", "t(i)")
    print("------------------------------------------------------------------------")
    r, rr = a, b
    s, ss = 1, 0
    t, tt = 0, 1
    i = 0
    printEntry(i, r, "", s, t)
    while rr != 0:
        i += 1
        q = r/rr
        rrr = r % rr
        r, s, t, rr, ss, tt = rr, ss, tt, rrr, (s-ss*q), (t-tt*q)
        printEntry(i, r, q, s, t)
    printEntry(i+1, rr, "", ss, tt)
    d = r
    return (d, s, t)


def printEntry(i, r, q, s, t):
    print("%10s | %10s %10s %10s %10s" %(str(i), str(r), str(q), str(s), str(t)))


# EEA(1009, 469)