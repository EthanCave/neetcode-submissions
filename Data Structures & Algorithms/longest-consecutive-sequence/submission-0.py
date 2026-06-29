class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_sequence = 0
        current_sequence = 0
        for num in nums:
            current_sequence = 1
            if (num - 1) not in nums:
                while (num + 1) in nums:
                    current_sequence += 1
                    num += 1
                if current_sequence > max_sequence:
                    max_sequence = current_sequence
        return max_sequence

        