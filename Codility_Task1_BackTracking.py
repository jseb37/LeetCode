'''
Given an array consisting of N strings calculate length of longest string S which fulfills below conditions
S is concatenation of some of the strings from A
Every letter in s is different
if no such string exists function should return 0

'''

'''
To solve this problem, you can use a backtracking approach to explore all possible combinations of strings from the array. For each combination, check if the resulting concatenated string has all unique characters. If it does, keep track of its length and update the maximum length found so far.

Here's the step-by-step approach to solve this problem:

Define a helper function that checks if a string has all unique characters.
Use a backtracking function to generate all possible concatenations of strings.
For each concatenation, use the helper function to check if it has all unique characters.
Keep track of the maximum length of valid concatenations.
'''


def max_length_unique_chars(arr):
    # Helper function to check if a string has all unique characters
    def is_unique(s):
        return len(s) == len(set(s))

    # Backtracking function to explore all concatenations
    def backtrack(start, current):
        nonlocal max_length
        if is_unique(current):
            max_length = max(max_length, len(current))
        else:
            return

        for i in range(start, len(arr)):
            backtrack(i + 1, current + arr[i])

    max_length = 0
    backtrack(0, "")
    return max_length


# Example usage:
arr = ["abc", "de", "fgh"]
print(max_length_unique_chars(arr))  # Output: 8 (e.g., "abcdefgh")

'''
Explanation:
Helper function is_unique: This function checks if all characters in a string are unique by comparing the length of the string to the length of the set of its characters.
Backtracking function backtrack: This function explores all possible concatenations starting from the start index and builds the current concatenation string current.
If the current string has all unique characters, update the max_length.
If not, return immediately.
For each index i from start to the end of the array, call backtrack recursively with the next index and the concatenation of the current string and the i-th string from the array.
Initial call to backtrack: Start the backtracking with an empty string and from the 0th index.
This approach ensures that all possible combinations are explored and the maximum length of a valid concatenated string with all unique characters is found. If no such string exists, the function returns 0.
'''