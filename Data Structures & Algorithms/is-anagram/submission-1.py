class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_ct = {}
        t_ct = {}
        for i in range(len(s)):
            if s[i] in s_ct:
                s_ct[s[i]]+=1
            else:
                s_ct[s[i]]=1
            if t[i] in t_ct:
                t_ct[t[i]]+=1
            else:
                t_ct[t[i]]=1

        for k,v in s_ct.items():
            if k not in t_ct:
                return False
            if t_ct[k] != v:
                return False

        return True