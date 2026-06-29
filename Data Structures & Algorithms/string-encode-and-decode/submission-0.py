class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        encoded_string = []
        for string in strs:
            encoded_string.append(str(len(string)) + ",")
        encoded_string.append("#")
        for string in strs:
            encoded_string.append(string)
        return ''.join(encoded_string)


    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, res, i = [], [], 0
        while s[i] != "#":
            j = i
            while s[j] != ",":
                j += 1
            sizes.append(int(s[i:j]))
            i = j + 1
        i += 1
        for sz in sizes:
            res.append(s[i:i + sz])
            i += sz
        return res



