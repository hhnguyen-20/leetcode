class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n not in visit:
            visit.add(n)

            lst = list(map(int, str(n)))
            res = sum([i**2 for i in lst])
            
            if res == 1:
                return True
            
            n = res
        
        return False

