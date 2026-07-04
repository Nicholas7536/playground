class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        two = heapq.nlargest(k,nums)
        return two[-1]