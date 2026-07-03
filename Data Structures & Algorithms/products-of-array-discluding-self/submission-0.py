class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nump=1
        l=len(nums)
        flag=1
        numss=[]
        for i in range(l):
            if nums[i]==0:
                flag=0
                for j,num in enumerate(nums):
                    if j !=i:
                        nump *=num
                numss=[0]*l
                numss[i]=nump
                break
        
        if flag==1:
            for num in nums:
                nump *=num
            numss=[nump//num for num in nums]

        return numss