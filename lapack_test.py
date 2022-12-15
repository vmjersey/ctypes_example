#!/bin/env python3
import c_utils

f = c_utils.lapack()

a = [
       6.80, -2.11,  5.66,  5.97,  8.23,
       -6.05, -3.30,  5.36, -4.44,  1.08,
       -0.45,  2.58, -2.70,  0.27,  9.04,
       8.32,  2.71,  4.35, -7.17,  2.14,
       -9.67, -5.14, -7.26,  6.08, -6.87
]

b = [
       4.02,  6.19, -8.22, -7.57, -3.03,
       -1.56,  4.00, -8.67,  1.75,  2.86,
       9.81, -4.09, -4.57, -8.61,  8.99
]

rows = 5
cols = 5
nrhs = 3 
lda = 5
ldb = 5


answer = f.dgesv(a,b,rows,cols,lda,ldb)

for i in range(rows):
    print(i,":",end="   ")
    for j in range(nrhs):
        print(answer[i+j*lda],end=" ")
    print("\n")
