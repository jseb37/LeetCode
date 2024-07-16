'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''

'''    
[1,2,3,4,5]

[1,1,2,6,24] - #Left Array

[1,5,20,60,120] 

Reverse above array 

[120,60,20,5,1] - #Right Array 

Multiply both left and right array , index by index and store in output array


As we have 1 already appended to array,when looped from first index, the product of last value in left array and value at current index will 
be product of all values behind that particular index

Similary in right array


'''


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [1]
        right = [1]
        output = []

        # Left array
        for i in range(len(nums)-1):
            left.append(left[-1] * nums[i])
        print(left)
        #Right array
        for i in range(len(nums)-1, 0, -1):
            right.append(right[-1] * nums[i])
        print(right)
        right = right[::-1]


        for i in range(len(nums)):
            output.append(left[i] * right[i])
        return output


so = Solution()
nums = [1,2,3,4,5]
output=so.productExceptSelf(nums)
print(output)
