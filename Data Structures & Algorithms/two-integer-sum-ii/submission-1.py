class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=1
        r=len(numbers)
        while l<r:
            if numbers[l-1]+numbers[r-1]>target:
                r=r-1
            elif numbers[l-1]+numbers[r-1]<target:
                l=l+1
            else:
                break
        return [l,r]
            