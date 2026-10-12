class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)
        inc = [False] * n
        dec = [False] * n

        inc[0] = True
        for i in range(1, n):
            inc[i] = inc[i - 1] and nums[i - 1] < nums[i]

        dec[n - 1] = True
        for i in range(n - 2, -1, -1):
            dec[i] = dec[i + 1] and nums[i] > nums[i + 1]
        
        pre = [0]*(n+1)
        for i in range( n):
            pre[i+1] = pre[i] + nums[i]
        ttl = pre[n]

        diff = float("inf")
        for i in range(n-1):
            if inc[i] and dec[i+1]:
                left = pre[i+1]
                right = ttl - left
                a = abs(right - left)
                if diff > a:
                    diff = a
        return diff if diff != float('inf') else -1