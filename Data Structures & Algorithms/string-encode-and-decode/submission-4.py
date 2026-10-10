class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for i in strs:
            res.append(str(len(i))+"#"+i)
        return "".join(res)


    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            # "5#Hello5#World"
            length = int(s[i:j])
            i = j+1
            item = s[i:i+length]
            print(item)
            i=i+length
            res.append(item)

        return res

