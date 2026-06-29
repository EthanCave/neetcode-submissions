class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = round(len(nums) - 1)
        if not nums:
            return -1
        if target < nums[mid]:
            return self.search(nums[:mid], target)
        if target > nums[mid]:
            return self.search(nums[mid:-1], target)
        return mid