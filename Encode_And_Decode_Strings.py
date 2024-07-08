'''
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode
Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]

'''
'''
length of string + # + string -> length for checking when next string starts and # for separation of strings

'''

class Solution:
    def encode(self,strs):
        res = ""
        for s in strs:
            res += str(len(strs)) + '#' + s
        return res

    def decode(self,s):
        res,i=[],0
        while i<len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j+1+length
        return res
s = Solution()
res_encode=(s.encode(["neet","code","love","you"]))
print(res_encode)
print(s.decode(res_encode))


