class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = {}
        for i in strs:
            sorted_word = ''.join(sorted(i))
            if a.get(sorted_word):
                a.get(sorted_word).append(i)
            else:
                a[sorted_word] = [i]
        return list(a.values())