'''
Suppose an array of length n sorted in ascrighting order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.

'''

'''
Core Concept

For rotated sorted array , if mid value of array is greater than last value it means minimum value is in second half of array.
In Rotated sorted array 2 halfs of array are sorted.

Exampe as shown below. This will be same case for even length array.
[3,4,5,1,2]  ----> Rotated 3 time
[2,3,4,5,1]  ----> Rotated 4 time

Then,we need to check for min value in second half of array (no need to check in 1st half of array) to reduce time complexity.

If mid value less than last value , we need to check on first half of array , right pointer change to mid,left pointer as it is

This process continue till left pointer less than right pointer if , both comes equal return num[right] which will be the minimum value

Why return num[right] not nums[mid] , it will give "local variable 'mid' referenced before assignment" error for array with single value say nums [1]
In this case it wont enter to while condition or mid value be assigned , therefor just return nums[right] or nums[0] which is 1
[1,2,3,4,5]  ----> Original Array
[5,1,2,3,4]  ----> Rotated 1 time
[4,5,1,2,3]  ----> Rotated 2 time
[3,4,5,1,2]  ----> Rotated 3 time
[2,3,4,5,1]  ----> Rotated 4 time
[1,2,3,4,5]  ----->Rotated 5 time



'''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[right]

s= Solution()
nums = [3,4,5,1,2]
print(s.findMin(nums))