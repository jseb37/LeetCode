# Iterative Binary Search Function method Python Implementation
# It returns index of n in given list1 if present,
# else returns -1
def binary_search(list1, n):
    left = 0
    right = len(list1) - 1
    while left <= right:
        # for get integer result
        mid = (left + right) // 2
        # Check if n is present at mid
        if list1[mid] == n:
            return mid
        # If n is greater, compare to the right of mid
        if list1[mid] < n:
            left = mid + 1
        # If n is smaller, compared to the left of mid
        elif list1[mid] > n:
            right = mid - 1
    return -1


# Initial list1
list1 = [12, 24, 32, 39, 45, 50, 54]
n = 45

# Function call
result = binary_search(list1, n)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in list1")