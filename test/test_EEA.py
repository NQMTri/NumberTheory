
import fractions
import pytest
import sys
import os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))
from EEA import *

image_path = './image/cat.jpg'

class TestEEA():
    def test_eea(self):
        for a, b in [(15,12), (17,14), (30, 20), (345, 219)]:
            d, s, t = EEA(a,b)
            assert d == fractions.gcd(a,b)
            assert (a*s + b*t) == d
            print ('\na, b = (%d, %d)'%(a,b))
            print ('d ,s, t = %d %d %d'%(d, s, t))

