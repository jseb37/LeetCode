'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
'''

'''

Time complexity - logm + logn - log(m*n)

logm - To find element is in which row
logn - To find element in the specific row

Double binary search

'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #Get dimensions of matrix - rows and coloumns
        #First binary search - To find target row or to check if target row doesnt exist
        ROWS,COLS = len(matrix),len(matrix[0])
        top,bot = 0,ROWS-1
        while top <= bot:
            midrow = (top + bot) // 2
            #Check if target value greater than rows last value , if greater go to next row , ie top = midrow + 1
            if target > matrix[midrow][-1]:
                top = midrow + 1
            # Check if target value less than rows first value , if greater go to next row , ie bot = midrow - 1
            elif target < matrix[midrow][0]:
                bot = midrow -1
            #It will go to below condition when value is in this midrow.
            #Target is not less than first value of midrow or greater than last value of this midrow.
            #We can break from this first binary search of finding the target row as we have found the target row
            #And move to second binary search which will be done on the target row
            else:
                break
        #If none of the rows contain the target value below condition is executed,when top pointer crosses bottom pointer
        if not(top <= bot):
            return False
        #Second binary search in target row [Normal binary search with change in right pointer]
        left,right = 0,COLS -1
        while left <= right:
            mid = (left + right) // 2
            if target > matrix[midrow][mid]:
                left = mid + 1
            elif target < matrix[midrow][mid]:
                right = mid - 1
            else:
                return True
        return False

s = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(s.searchMatrix(matrix,3))