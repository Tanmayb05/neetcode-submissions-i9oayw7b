class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeroes = 0
        for i in nums:
            if i:
                product *= i
            else:
                zeroes += 1
        
        print(product)
        res = [0] * len(nums)
        if zeroes > 1: return res

        for i,c in enumerate(nums):
            if zeroes:
                res[i] = 0 if c else product
            else:
                res[i] = product // c
        print(res)
        return res