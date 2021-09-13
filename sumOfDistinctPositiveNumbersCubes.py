"""
Check if a number is a sum of distinct positive numbers' cubes.
You have to tell how many possibles solutions.

Example : 9 = 1³ + 2³
(1,2) and (2,1) are the the same answer and count only once.

Note that we only consider here sums with at least two operands.
Input
Integer N
Output
Integer R
Constraints
N < 10000
Example
Input
9
Output
1
"""

from itertools import combinations
n=int(input())
l=[i**3 for i in range(1,int(n**(1/3))+1)]
print(sum([list(map(sum,combinations(l,i))).count(n) for i in range(1,len(l)+2)]))
