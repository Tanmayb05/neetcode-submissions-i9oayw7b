class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashSet = {}
        for i in range(len(nums)):
            hashSet[nums[i]] = i
        print(hashSet)
        for i in range(len(nums)):
            if (target - nums[i]) in hashSet.keys() and i != hashSet[target-nums[i]]:
                print(i, nums[i], hashSet[target-nums[i]])
                return list(set([i, hashSet[target-nums[i]]]))