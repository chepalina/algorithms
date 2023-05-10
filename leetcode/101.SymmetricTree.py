# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        left_stack = [root.left]
        right_stack = [root.right]

        while left_stack and right_stack:
            left = left_stack.pop()
            right = right_stack.pop()

            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False

            left_stack.append(left.left)
            left_stack.append(left.right)

            right_stack.append(right.right)
            right_stack.append(right.left)

        if not left_stack and not right_stack:
            return True
        else:
            return False





    # def sym(self, a: Optional[TreeNode], b: Optional[TreeNode]):
    #     if not a and not b:
    #         return True

    #     if a and not b:
    #         return False

    #     if not a and b:
    #         return False

    #     if a.val != b.val:
    #         return False

    #     return self.sym(a.right, b.left) and self.sym(b.right, a.left)



    # def isSymmetric(self, root: Optional[TreeNode]) -> bool:

    #     if root is None:
    #         return False

    #     return self.sym(root.left, root.right)