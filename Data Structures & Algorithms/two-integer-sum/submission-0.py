class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_num = {}
        for i in range(len(nums)):
            if nums[i] in target_num:
                return [target_num[nums[i]], i]
            target_num[target - nums[i]] = i
        return [0,0]
        