class Solution:
    def isValid(self, s: str) -> bool:
        valid_mappings = {
        "}" : "{",
        ")" : "(",
        "]" : "["}
        stack = []
        for bracket in s:
            if bracket in valid_mappings:
                if stack and stack[-1] == valid_mappings[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        return True if not stack else False