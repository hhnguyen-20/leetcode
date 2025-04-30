class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        result = 0
        i = 0

        for _ in range(len(nums)):
            if nums[i] != val: 
                result += 1
                i += 1
            else:
                nums.remove(nums[i])

        return result
