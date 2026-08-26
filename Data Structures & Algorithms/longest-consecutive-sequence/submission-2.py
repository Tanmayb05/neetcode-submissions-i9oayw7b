class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for i in nums:
            length = 1
            # previous number is not present in set, 
            # that means the current number is a start of a new sequence
            if (i-1) not in nums_set:
                while (i+1) in nums_set:
                    length += 1
                    i += 1
            longest = max(length, longest)
        return longest