class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for i in strs:
            sortedS = ''.join(sorted(i))
            output[sortedS].append(i)
        return list(output.values())