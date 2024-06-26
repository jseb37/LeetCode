'''
 Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''
'''
Certainly! The line of code freq = [[] for i in range(len(nums) + 1)] is a list comprehension in Python, and it can be broken down as follows:

len(nums) + 1:

len(nums) calculates the number of elements in the list nums.
len(nums) + 1 adds 1 to this length. This is often done to create a list that has one more element than the original list nums.
for i in range(len(nums) + 1):

range(len(nums) + 1) generates a sequence of numbers starting from 0 up to len(nums), inclusive. This means if nums has 3 elements, range(len(nums) + 1) will generate the sequence [0, 1, 2, 3].
The for i in part iterates over each number in this sequence. The variable i takes each value in the sequence one by one.

[[] for i in range(len(nums) + 1)]:

This is a list comprehension that creates a new list.
For each value of i generated by the range, an empty list [] is created.
This results in a list of empty lists. The length of the outer list will be len(nums) + 1.

Initialize a list with zeros:
freq = [0 for i in range(len(nums) + 1)] 

freq = [0, 0, 0, 0]
'''
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        #Why len(nums) + 1 - Because if there are 6 elements in array, there can be 0 count  till 6 count ,so 7

        print(freq)
        # index of freq will be count of element and value will be list of elements with that count
        #[[]
         #[]
         #[]]
        #It will be 2d array with index - freq of element and column - the elements with that frequency
        #We will append the elements with that frequency and this will be column of 2D array
        for n in nums:
            count[n] = 1 + count.get(n,0)
        print(count)
        for n ,c in count.items():
            freq[c].append(n)
        print(freq)
        res = []
        for i in range(len(freq)-1 ,0 ,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


so = Solution()
res = so.topKFrequent([1,1,1,2,2,3] , 2)
print(res)