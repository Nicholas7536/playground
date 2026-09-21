class Solution:
    def canJump(self, nums: list[int]) -> bool:
        stepRem = 0
        length = len(nums)-1
        for i in range(len(nums)):
            stepRem = max(stepRem, nums[i])
            if stepRem == 0 and i < length:
                return False
            stepRem -= 1
        return True
    
    '''
    max of remaining steps and curr steps
    [2,3,1,1,4] - 
    idx0, 0 step remaining; 2 steps curr (max = 2) - 
    idx1, 1 step remaining; 3 steps curr (max = 3) - 
    idx2, 2 steps remaining; 1 step curr (max = 2)

    [3,2,1,0,4]
    idx0, 0 step remaining; 3 steps cur (max=3) -
    idx1, 2 step remaining; 2 steps cur (max=2) - 
    idx2, 1 step remaining; 1 step cur( max=1) - 
    idx3, 0 step remaining; 0 step cur (max = 0) - if max=0 function occurs before end of list return false
    '''

    
