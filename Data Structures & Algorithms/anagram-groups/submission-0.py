class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_list = []
        letter_occurance_map = {}
        index = 0
        def getFrequency(word: str) -> tuple:
            letter_occurance = [0] * 26
            for letter in word:
                letter_occurance[ord(letter) - ord('a')] += 1
            return tuple(letter_occurance)
        for word in strs:
            frequency = getFrequency(word)
            if frequency not in letter_occurance_map:
                letter_occurance_map[frequency] = index
                anagram_list.append([])
                index += 1
            anagram_list[letter_occurance_map[frequency]].append(word)
        return anagram_list