# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node, max_so_far):
            if not node:
                return 0

            is_good = False
            if node.val >= max_so_far:
                is_good = True

            new_max = max(max_so_far, node.val)

            left_count = helper(node.left, new_max)
            right_count = helper(node.right, new_max)

            total = int(is_good) + left_count + right_count
            return total

        return helper(root, root.val)