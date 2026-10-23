class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        slowest_ahead = 0.0
        for p, s in sorted(zip(position, speed), reverse=True):
            t = (target - p) / s
            if t > slowest_ahead:
                fleets += 1
                slowest_ahead = t
        return fleets