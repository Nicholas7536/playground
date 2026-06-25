# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = [root]
        righted = []

        while queue:
            level = []
            for _ in range(len(queue)):   
                top = queue.pop(0)        
                if not top:
                    continue
                level.append(top.val)
                queue.append(top.left)
                queue.append(top.right)
            
            if level:                    
                res.append(level)
        for i in res:
            righted.append(i[-1])
        
        return righted