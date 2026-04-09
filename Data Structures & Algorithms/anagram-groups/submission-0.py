class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for str in strs:
            if "".join(sorted(str)) in anagram.keys():
                anagram["".join(sorted(str))].append(str)
            else:
                anagram["".join(sorted(str))] = [str]

        return list(anagram.values())
        