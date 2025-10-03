class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.strip().split()
        dict = {}

        if len(pattern) != len(words): return False
        if len(set(pattern)) != len(set(words)): return False

        for w, c in zip(words, pattern):
            if w not in dict:
                dict[w] = c
            elif dict[w] != c:
                return False
        
        return True
