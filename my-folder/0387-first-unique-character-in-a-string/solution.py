class Solution:
    def firstUniqChar(self, s: str) -> int:
        res = []

        unique_chars = set(s)
        for char in unique_chars:
            if s.count(char) == 1:
                res.append(s.find(char))

        if res:
            return min(res)
        else:
            return -1      
