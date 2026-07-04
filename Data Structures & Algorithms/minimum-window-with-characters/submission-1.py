class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT={}
        for i in t:
            countT[i]=1+countT.get(i,0)
        windows={}
        need=len(countT)
        res=[-1,-1]
        min_len=float("infinity")
        l=have=0
        for r in range(len(s)):
            c=s[r]
            windows[c]=1+windows.get(c,0)

            if c in countT and countT[c]==windows[c]:
                have +=1
            
            while have==need:
                if r-l+1<min_len:
                    res=[l,r]
                    min_len=r-l+1
                
                windows[s[l]]=windows[s[l]]-1
                if s[l] in countT and windows[s[l]] < countT[s[l]]:
                    have -=1
                l+=1
        l,r=res
        return s[l:r+1] if min_len!=float("infinity") else ""

            
