class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix_candidate = strs[0]
        for string in strs:
            while not string.startswith(prefix_candidate):
                prefix_candidate = prefix_candidate[:-1]
        return prefix_candidate

        