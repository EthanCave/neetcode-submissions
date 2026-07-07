class Solution:
    def isHappy(self, n: int) -> bool:
        seen_nums = set()
        num = n
        while num not in seen_nums:
            print(num)
            print(seen_nums)
            if num == 1:
                return True
            seen_nums.add(num)
            num = 0
            for digit in str(n):
                num += int(digit)**2
            n = num
        print(num, seen_nums)
        return False





        