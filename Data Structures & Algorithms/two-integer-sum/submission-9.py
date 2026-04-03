class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {} 
        # val -> index
        for i, n in enumerate(nums):
            to_find = target - n
            if to_find in hash_map:
                return [hash_map[to_find], i]
            hash_map[n] = i

