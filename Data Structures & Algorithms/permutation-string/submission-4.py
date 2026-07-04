class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        dict1={}
        dict2={}

        for s in s1:
            dict1[s]=1+dict1.get(s,0)

        for r in range(len(s2)):
            if dict1==dict2:
                return True
            elif s2[r] not in dict1.keys():
                l=r+1
                dict2={}
            else:
                if dict2.get(s2[r],0) ==dict1[s2[r]]:
                    while s2[l] != s2[r]:
                        dict2[s2[l]]=dict2[s2[l]]-1
                        l+=1
                    l+=1
                else:
                    dict2[s2[r]]=1+dict2.get(s2[r],0)
            if dict1==dict2:
                return True

        return False

