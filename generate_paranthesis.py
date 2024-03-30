'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8
For n = 2, the recursion tree will be something like this,
								   	(0, 0, '')
								 	    |
									(1, 0, '(')
								   /           \
							(2, 0, '((')      (1, 1, '()')
							   /                 \
						(2, 1, '(()')           (2, 1, '()(')
						   /                       \
					(2, 2, '(())')                (2, 2, '()()')
						      |	                             |
					res.append('(())')             res.append('()()')

'''
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def dfs(left,right,s):
            if len(s) == n*2:
                res.append(s)
                return
            if left < n:
                dfs(left+1,right,s+'(')

            if right<left:
                dfs(left,right+1,s+')')

        res=[]
        dfs(0,0,'')
        return res


s=Solution()
print(s.generateParenthesis(3))