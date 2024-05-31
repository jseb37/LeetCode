'''
Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
'''

A = [1, 3, 6, 4, 1, 2]

# Create a set of all positive integers in the array
positive_integers = set(x for x in A if x > 0)

# Start checking from 1 upwards to find the smallest missing positive integer
smallest_missing = 1
while smallest_missing in positive_integers:
   smallest_missing += 1
print(smallest_missing)

