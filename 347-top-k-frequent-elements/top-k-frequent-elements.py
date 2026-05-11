class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        occur = {}
        for num in nums:
            occur[num] = occur.get(num, 0) + 1

        bucket = [[] for _ in range(n+1)]

        for key in occur:
            bucket[occur[key]].append(key)

        res = []
        for i in range(n, 0, -1):
            if len(res) >= k:
                break
            for val in bucket[i]:
                res.append(val)
        return res
'''
[1,2,2,3,3,3] k=2

key = Frequency[0, 1, 2, 3, 4, 5, 6]
               [x, 1, 2, 3]
for range k get key
'''