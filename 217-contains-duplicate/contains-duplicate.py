class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dupe = set()

        for i in nums:
            if i in dupe:
                return True
            else: 
                dupe.add(i)
        return False