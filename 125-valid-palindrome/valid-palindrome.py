class Solution:
    def isPalindrome(self, s: str) -> bool:
        ctxt = "".join(filter(str.isalnum, s.lower()))

        i = 0
        j = len(ctxt)-1

        while i<j:
            if ctxt[i]!=ctxt[j]:
                return False
            i+=1
            j-=1
        return True