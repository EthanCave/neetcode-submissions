class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        running = 0
        for num in range(len(nums)):
            running = nums[num] ^ running
        return running
