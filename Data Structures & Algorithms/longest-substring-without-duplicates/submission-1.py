class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        dict1={}
        len_m=0
        for i,n in enumerate(s):
            if n in dict1 and dict1[n]>=left:
                left=dict1[n]+1
            dict1[n]=i
            len_m=max(len_m,i-left+1)
        return len_m

        