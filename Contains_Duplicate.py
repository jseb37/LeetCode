'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            else:
                hashset.add(n)    
        return False        


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = dict()
        for n in nums:
            count[n] = 1 + count.get(n,0)
            if count[n]>=2:
                return True
        return False

s = Solution()
nums = [1,1,1,3,3,4,3,2,4,2]
res = s.containsDuplicate(nums)
print(res)


#Using set

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_set = set(nums)
        if len(nums_set) != len(nums):
            return True
        else:
            return False

