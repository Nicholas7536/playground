class Solution:

    def search(self, nums: List[int], target: int) -> bool:

        nums.sort()

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return True

            elif target < nums[mid]:
                right = mid - 1

            else:
                left = mid + 1

        return False