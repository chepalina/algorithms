# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Time = O(N), Space = O(1) ?

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        left_gen = self.get_next(root)
        right_gen = self.get_reverse(root)
        left = next(left_gen)
        right = next(right_gen)

        while left.val!=right.val:
            temp_sum = left.val + right.val
            if temp_sum == k:
                return True

            if temp_sum < k:
                left = next(left_gen)
            else:
                right = next(right_gen)

        return False


    def get_next(self, root):
        if root:
            yield from self.get_next(root.left)
            yield root
            yield from self.get_next(root.right)

    def get_reverse(self, root):
        if root:
            yield from self.get_reverse(root.right)
            yield root
            yield from self.get_reverse(root.left)





        


