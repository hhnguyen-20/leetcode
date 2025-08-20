class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = 0
        for c in ransomNote:
            if c in magazine:
                magazine = magazine.replace(c, '', 1)
                count += 1
        
        return count == len(ransomNote)
        
