1. Warup with Lists 

2. Birthday Paradox(something its tough to beilive but its true)

    In probability theory, the birthday problem asks for the probability that, in a set of n randomly chosen people, at least two will share a birthday. The 
    birthday   paradox is that, counterintuitively, the probability of a shared birthday exceeds 50% in a group of only 23 people.

3. Naive Search in a List

4. The Obvious Sort

5. The matrix Dot Product

6. Matrix Addition



7. Matrix Multiplication
<img width="841" alt="Screenshot 2022-01-19 at 7 38 04 AM" src="https://user-images.githubusercontent.com/52348635/150050188-8e574839-4607-4232-bb3c-f640a6034601.png">



```python

r1 = [1,2,3]
r2 = [4,5,6]
r3 = [7,8,9]

s1 = [1,2,1]
s2 = [6,2,3]
s3 = [4,2,1]

A = []
B = []
A.append(r1)
A.append(r2)
A.append(r3)
B.append(r1)
B.append(r2)
B.append(r3)

C = [[0,0,0],[0,0,0],[0,0,0]]

dim = 3

# C[i][j] is the dot product of the ith row of A
# and the jth column of B

for i in range(dim):
    for j in range(dim):
        for k in range(dim):
            C[i][j] = C[i][j] + A[i][k]*B[k][j]
        



#C[i][j] = dot product of A[i][:] and B[:][j]
print(C)

```
