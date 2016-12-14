import math
def EEA(a, b):
    if (a < b):
        t = a
        a = b
        b = t

    r = a
    r1= b
    s = 1
    s1= 0
    t = 0
    t1= 1
    while r1 != 0:
        q = r/r1
        r2 = r % r1
        tmp_s1 = s - s1*q
        tmp_t1 = t - t1*q
        r = r1
        s = s1
        t = t1
        r1 = r2
        s1 = tmp_s1
        t1 = tmp_t1
    d = r
    return (d, s, t)

d, s, t = EEA(15, 12)
print (d, s, t)
