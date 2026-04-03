class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        result = -1
        while left<=right:
            middle = int((left+right)/2)
            if nums[middle]<target:
                left = middle + 1
            elif nums[middle]==target:
                result = middle
                break
            else:
                right = middle - 1
        return result
            