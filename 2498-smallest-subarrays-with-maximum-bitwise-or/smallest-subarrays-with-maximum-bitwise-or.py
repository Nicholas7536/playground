class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        def getPos(n):
            ret = [0] * 32
            i = 0
            while n:
                ret[i] = n % 2
                n = n // 2
                i += 1
            return ret
        def add(arr1, arr2):
            for i in range(32):
                arr1[i] += arr2[i]
        def sub(arr1, arr2):
            for i in range(32):
                arr1[i] -= arr2[i]
        def needed(arr1, arr2):
            for a1, a2 in zip(arr1, arr2):
                if (a1-a2 == 0) != (a1 == 0):
                    return True
            return False
        n = len(nums)
        cur, r = getPos(nums[-1]), n-1
        ans = [1]
        for l in range(n-2, -1, -1):
            add(cur, getPos(nums[l]))
            while r>l and not needed(cur, getPos(nums[r])):
                sub(cur, getPos(nums[r]))
                r -= 1
            ans.append(r-l+1)
        return ans[::-1]

