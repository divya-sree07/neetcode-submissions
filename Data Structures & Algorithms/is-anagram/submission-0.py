class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hp={}
        if len(s)!=len(t):
            return False
        for i in t:
            if i in hp:
                hp[i]=hp[i]+1
            else:
                hp[i]=1
        for i in s:
            if i in hp:
                hp[i]=hp[i]-1
            else:
                return False
        for i in hp:
            if hp[i]!=0:
                return False
        return True
