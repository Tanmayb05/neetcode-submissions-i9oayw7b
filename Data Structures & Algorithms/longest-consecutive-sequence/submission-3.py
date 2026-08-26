class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for i in nums:
            # previous number is not present in set, 
            # that means the current number is a start of a new sequence
            if (i-1) not in nums_set:
                length = 1
                while (i+length) in nums_set:
                    length += 1
                longest = max(length, longest)
        return longest