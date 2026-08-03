class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        l, r = 1, max_pile
        while l < r:
            mid = (l + r) // 2
            temp_h = h
            for j in piles:
                temp_h -= -(-j//mid)
            if temp_h >= 0:
                r = mid
            else:
                l = mid + 1
            
        return l

