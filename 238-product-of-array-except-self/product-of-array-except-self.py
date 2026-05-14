class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        eg: 1 [2,3,4,5]
      >   P=6 [1,2,6,24]
      >   O=60 [60,40,30,24]
        '''
        prefix = 1
        postfix = 1
        output = []
        for i in range(len(nums)):
            output.append(prefix)
            prefix*=nums[i]
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        
        return output
