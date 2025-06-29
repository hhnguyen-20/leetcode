class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split(' ')
        
        result = [w for w in s_list if w != '']

        return ' '.join(result[::-1])
