class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict={}
        for num in nums:
            num_dict[num]=1+num_dict.get(num,0)
        
        out=[]
        for key,v in sorted(num_dict.items(),key=lambda x:x[1],reverse=True):
            if len(out)<k:
                out.append(key)
            else:
                break
        return out