'''

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''

from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groupAnagramsdic = defaultdict(list)
        print(groupAnagramsdic)

        for word in strs:
            #Key of below groupAnagramsdic will be the sorted word , which can be used to append anagram words
            #Why using join?? - If u dont convert this to string via join it will give below error
            #TypeError: unhashable type: 'list'
            #The “TypeError: unhashable type: 'list'” error is raised when you try to assign a list as a key in a dictionary
            #To solve this error, ensure you only assign a hashable object, such as a string or a tuple, as a key for a dictionary
            #groupAnagramsdic[sorted(word)].append(word)


            groupAnagramsdic["".join(sorted(word))].append(word)
        print(groupAnagramsdic)
        return groupAnagramsdic.values()


s = Solution()
res=s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(res)