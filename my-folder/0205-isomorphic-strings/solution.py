class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        if len(set(s)) != len(set(t)): return False

        dict = {}

        for a, b in zip(s, t):
            if a not in dict:
                dict[a] = b
            elif dict[a] != b:
                return False
        
        return True
