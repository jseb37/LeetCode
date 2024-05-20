'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.



Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1


Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
'''

#Solution with hashmap - but uses o(n) - memory

class Solution:
    def singleNumber(self, nums):
        dict = {}

        for i in nums:
            dict[i] = dict.get(i, 0) + 1

        for k, v in dict.items():
            if v == 1:
                return k

#Solution using XOR - o(1) - Memory
#xor same number results in zero , xor 0 with number gives number
#1 xor 1 is 0 , 1 xor 0 is 0

class Solution:
    def singleNumber(self, nums):
        a = 0
        for i in nums:
            a = a^i
        return a