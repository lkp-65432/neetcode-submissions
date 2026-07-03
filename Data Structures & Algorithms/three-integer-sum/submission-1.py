class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num1=sorted(nums)
        l=len(num1)
        output=[]
        for i in range(l):
            flag=num1[i]
            if i!=0 and flag==num1[i-1]:
                continue
            lef=i+1
            rig=l-1
            while lef<rig:
                if num1[lef]+num1[rig]>-flag:
                    rig=rig-1
                elif num1[lef]+num1[rig]<-flag:
                    lef=lef+1
                else:
                    flag1=num1[lef]
                    flag2=num1[rig]
                    if (lef != i+1 and flag1==num1[lef-1]):
                        lef =lef+1
                    elif (rig != l-1 and flag2==num1[rig+1]):
                        rig=rig-1
                    else:
                        output.append([flag,flag1,flag2])
                        rig=rig-1
        return output
            
        
