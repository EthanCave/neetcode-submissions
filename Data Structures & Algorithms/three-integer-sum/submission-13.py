class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sum_list = []
        for num_index in range(len(nums) - 2):
            candidate = nums[num_index]
            l = num_index + 1
            r = len(nums) - 1
            while l < r:
                if candidate + nums[l] + nums[r] > 0:
                    r -= 1
                elif candidate + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    if [candidate, nums[l], nums[r]] not in sum_list:
                        sum_list.append([candidate, nums[l], nums[r]])
                    l += 1
        return sum_list
            
        