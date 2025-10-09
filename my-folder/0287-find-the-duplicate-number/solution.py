class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums = sorted(nums)

        start = nums[0]

        for n in nums[1:]:
            if n == start:
                return n
            else:
                start = n
