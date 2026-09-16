class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        l, r = 0, len(height) - 1
        maxLeft = height[l]
        maxRight = height[r]
        while l < r:
            maxLeft = max(height[l], maxLeft)
            maxRight = max(height[r], maxRight)
            water = min(maxLeft, maxRight)
            if water > height[l]:
                total += water - height[l]
            elif water > height[r]:
                total += water - height[r]
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return total


        