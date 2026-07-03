class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num1=set(nums)
        longest=0
        for num in num1:
            if num-1 not in num1:
                now_num=num
                now_len=1

                while now_num+1 in num1:
                    now_num +=1
                    now_len +=1
                
                longest=max(now_len,longest)
        return longest