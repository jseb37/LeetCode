'''
You are given a string s consisting of lowercase English letters.

Your task is to find the maximum difference diff = freq(a1) - freq(a2) between the frequency of characters a1 and a2 in the string such that:

a1 has an odd frequency in the string.
a2 has an even frequency in the string.
Return this maximum difference.

 

Example 1:

Input: s = "aaaaabbc"

Output: 3

Explanation:

The character 'a' has an odd frequency of 5, and 'b' has an even frequency of 2.
The maximum difference is 5 - 2 = 3.
Example 2:

Input: s = "abcabcab"

Output: 1

Explanation:

The character 'a' has an odd frequency of 3, and 'c' has an even frequency of 2.
The maximum difference is 3 - 2 = 1.
 

Constraints:

3 <= s.length <= 100
s consists only of lowercase English letters.
s contains at least one character with an odd frequency and one with an even frequency.

'''

class Solution:
    def maxDifference(self, s: str) -> int:
        my_dict = {}
        min_even = len(s)
        max_odd = 0
        for char in s:
            my_dict[char] = 1 + my_dict.get(char,0)
        print(my_dict)
        for v in my_dict.values():
            if v % 2 == 0:
                min_even = min(min_even,v)
            else:
                max_odd = max(max_odd,v)
        return (max_odd - min_even)
