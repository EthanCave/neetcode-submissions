class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        cur_area = (r - l ) * min(heights[l], heights[r])
        while l < r:
            print(l , r)
            r_area = (r - l - 1) * min(heights[l], heights[r - 1])
            l_area = (r - l - 1) * min(heights[l + 1], heights[r])
            if r_area > cur_area:
                print("r_area > cur_area")
                cur_area = r_area
                r -= 1
            if l_area > cur_area:
                print("l_area > cur_area")
                cur_area = l_area
                l += 1
            else:
                if heights[l] > heights[r]:
                    r -= 1
                else:
                    l += 1
        return cur_area
        