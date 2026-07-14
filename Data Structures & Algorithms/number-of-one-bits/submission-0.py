class Solution:
    def hammingWeight(self, n: int) -> int:
        sum_ones = 0 
        n = bin(n)
        print(n)
        for digit in n:
            if digit == "1":
                sum_ones += 1
        return sum_ones