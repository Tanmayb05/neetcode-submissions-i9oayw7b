class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i
        print(res)
        return res


    def decode(self, s: str) -> List[str]:
        i=0
        res = []
        while i < len(s):
            num = ""
            while s[i] != '#':
                num += s[i]
                i+=1
            i+=1
            len_s1 = int(num)
            print(len_s1)
            s1 = s[i:i+len_s1]
            res.append(s1)
            print(res)
            i += len_s1


        return res



