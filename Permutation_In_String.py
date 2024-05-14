'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.



Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false


Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
'''


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        len(s1)
        dic_s2 = {}
        dic_s1 = {}
        l = 0
        for char in set(s1 + s2):
            dic_s2[char] = 0
            dic_s1[char] = 0

        for char in s1:
            dic_s1[char] += 1

        if len(s2) < len(s1):
            return False

        for i in range(len(s1)):
            dic_s2[s2[i]] += 1

        if dic_s2 == dic_s1:
            return True

        for i in range(len(s1), len(s2)):
            dic_s2[s2[l]] -= 1
            l += 1
            dic_s2[s2[i]] += 1
            if dic_s2 == dic_s1:
                return True
        return False

so = Solution()
s1 = "ab"
s2 = "eidbaooo"
print(so.checkInclusion(s1,s2))









