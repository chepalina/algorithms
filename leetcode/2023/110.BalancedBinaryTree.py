# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # abs(max(left) - max(right)) <= 1 -> True

        if not root:
            return True

        return abs(self.maxDepth(root.left) - self.maxDepth(root.right)) <= 1

    def maxDepth(self, root):

        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
