# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, min_val, max_val):
            if not node:
                return True

            is_valid = False
            if node.val > min_val and node.val < max_val:
                is_valid = True

            left_valid = helper(node.left, min_val, node.val)
            right_valid = helper(node.right, node.val, max_val)

            return is_valid and left_valid and right_valid

        return helper(root, float('-inf'), float('inf'))