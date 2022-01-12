import random

# Matrix Addition by first principles 

r1 = [1,2,3]
r2 = [4,5,6]
r3 = [7,8,9]

s1 = [1,2,1]
s2 = [6,2,3]
s3 = [4,2,1]

A = []
A.append(r1)
A.append(r2)
A.append(r3)

B = []
B.append(s1)
B.append(s2)
B.append(s3)


print(A)

print(B)

C = [[0,0,0],[0,0,0],[0,0,0]]

dim = 3

# C[2][1] is the dot product of the 2nd row of A and the 1th column of B

for i in range(dim):
    for j in range(dim):
        #C[i][j] = A[i][] . B[][j]
        for k in range(dim):
            C[i][j] += A[i][k]*B[k][j]

print(C)
