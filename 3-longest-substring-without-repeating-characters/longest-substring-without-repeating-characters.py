class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        seen = set()
        res = 0

        while r<len(s):
            print(seen,l,r)
            if s[r] not in seen:
                seen.add(s[r])
                res = max(res, r - l + 1)
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l+=1
                seen.add(s[r])
            r+=1
        return res