class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliment = {}

        for i in range(len(nums)):
            c = target - nums[i]
            if c in compliment:
                return [compliment[c], i]
            compliment[nums[i]] = i
