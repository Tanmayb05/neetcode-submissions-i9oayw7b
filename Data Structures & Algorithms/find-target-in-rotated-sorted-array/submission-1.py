class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0; right = len(nums)-1

        while left < right:
            middle = left + (right - left)//2
            if nums[middle] < nums[right]:
                right = middle
            else:
                left = middle+1
        
        pivot = left
        left = 0; right = len(nums)-1
        if nums[pivot]<=target and target<=nums[right]:
            left = pivot
        else:
            right = pivot - 1

        
        while left <= right:
            middle = left + (right-left)//2
            if nums[middle] < target:
                left = middle+1
            elif target < nums[middle]:
                right = middle-1
            else:
                return middle
        
        return -1