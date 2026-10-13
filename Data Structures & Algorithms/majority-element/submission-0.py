class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = {}
        for i in nums:
            a[i] = a.get(i,0) + 1
        print(nums)
        for i, n in a.items():
            if n>len(nums)/2:
                return i
        return -1