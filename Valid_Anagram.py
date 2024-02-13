'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
'''


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dicti1 = {}
        dicti2 = {}
        for i in s:
            if i in dicti1:
                dicti1[i] += 1
            else:
                dicti1[i] = 0
        for j in t:
            if j in dicti2:
                dicti2[j] += 1
            else:
                dicti2[j] = 0

        if dicti1 == dicti2:
            return True
        else:
            return False

s = "anagram"
t = "nagaram"
so=Solution()
res=so.isAnagram(s,t)
print(res)