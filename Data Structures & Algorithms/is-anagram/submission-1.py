class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=len(s)
        b=len(t)
        if a!=b:
            return False

        cout_s={}
        cout_t={}

        for i in range(a):
            cout_s[s[i]]=1+cout_s.get(s[i],0)
            cout_t[t[i]]=1+cout_t.get(t[i],0)
        return cout_s==cout_t
        