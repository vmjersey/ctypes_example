#!/bin/env python3
import c_utils



from c_utils import gsl

g = gsl()

a1 = (1, 2, 3, 4, 5)
a2 = (1, 2, 3, 6, 5)

answer = g.stats_correlation(a1,a2)

print(answer) 
