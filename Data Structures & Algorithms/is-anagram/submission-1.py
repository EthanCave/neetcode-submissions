class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        def build_hash(inp_str : str) -> dict:
            s_hash = {}
            for let1 in inp_str:
                if let1 in s_hash:
                    s_hash[let1] += 1
                else:
                    s_hash[let1] = 1
            return s_hash
        return build_hash(s) == build_hash(t)
            

            

        