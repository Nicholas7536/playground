class Solution:
    def isPalindrome(self, s):
        return s == s[::-1]

    def getAllParts(self, s, ans, parts):
        if len(s) == 0:
            ans.append(parts[:])  # copy, since parts keeps changing
            return
        for i in range(len(s)):
            part = s[:i + 1]
            if self.isPalindrome(part):
                parts.append(part)
                self.getAllParts(s[i + 1:], ans, parts)
                parts.pop()  # undo, so the next prefix length starts clean

    def partition(self, s):
        ans = []
        parts = []
        self.getAllParts(s, ans, parts)
        return ans