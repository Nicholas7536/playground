class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        longest = 1

        l = 0
        r = 1
        currWindow = {s[0]}
        curr = 1
        while r<len(s):
            if s[r] in currWindow:
                curr = 1
                currWindow.clear()
                l+=1
                currWindow = {s[l]}
                r=l+1
            else:
                currWindow.add(s[r])
                r+=1
                curr+=1
                longest = max(longest,curr)
        return longest
