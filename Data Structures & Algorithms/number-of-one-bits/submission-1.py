class Solution:
    def hammingWeight(self, n: int) -> int:
        # b = bin(n)
        # sum = 0
        # for i in b[2:]:
        #     sum = sum + int(i)
        # return sum
        res = 0
        while n:
            res += n%2
            n = n >> 1
        return res