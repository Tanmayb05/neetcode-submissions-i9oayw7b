class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:
        a = sorted(stones, reverse=True)
        if len(a) == 2:
            return abs(a[0]-a[1])
        else:
            while len(a)>1:
                a = sorted(a,reverse=True)
                print(a)
                x = a.pop(0)
                y = a.pop(0)
                b = abs(x-y)
                if b>0:
                    a.append(b)
            if not a:
                return 0
            print(a)
            return a[0]

        