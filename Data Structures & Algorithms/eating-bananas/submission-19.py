class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        l, r = 1, max_pile
        while l < r:
            mid = (l + r) // 2
            hours = sum(-(-p // mid) for p in piles)
            if hours <= h:
                r = mid
            else:
                l = mid + 1
            
        return l

