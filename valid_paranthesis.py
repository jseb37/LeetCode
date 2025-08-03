# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

# Example 5:

# Input: s = "([)]"

# Output: false

 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.


class Solution(object):
    def isValid(self, s):
        mapping = {'(':')','{':'}','[':']'}
        stack = []

        for ch in s:
            if ch in mapping:
                stack.append(ch)
            elif ch in mapping.values():
                if stack:
                   top = stack.pop()
                   if mapping[top]!=ch:
                      return False
                   else:
                      continue
                else:
                    return False
        return not stack






