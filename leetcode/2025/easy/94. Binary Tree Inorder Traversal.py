# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        stack = [(root, False)]
        result = []

        while stack:
            curr, seen = stack.pop()
            if curr.left is None or seen:
                result.append(curr.val)
                if curr.right is not None:
                    stack.append((curr.right, False))
            else:
                stack.append((curr, True))
                stack.append((curr.left, False))

        return result

    def inorderTraversal_rec(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def rec(node):
            if node is None:
                return

            rec(node.left)
            result.append(node.val)
            rec(node.right)

        rec(root)
        return result






