class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1

        current_digit = len(digits) - 1
        while digits[current_digit] == 10:
            digits[current_digit] = 0
            if current_digit == 0:
                digits.insert(0,1)
            else:
                current_digit -= 1
                digits[current_digit] += 1
        return digits