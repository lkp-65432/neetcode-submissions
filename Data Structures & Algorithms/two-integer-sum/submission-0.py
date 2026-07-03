class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i in range(len(nums)):
            c = nums[i]
            num = target - c
            if num in a:
                return [a[num], i]
            a[c] = i
        