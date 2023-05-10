# Definition for a binary tree node.

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


four = TreeNode(4, None, None)
three = TreeNode(3, None, None)
two = TreeNode(2, three, four)
one = TreeNode(1, None, two)

#    1
#   / \
#      2
#      /\
#     3  4


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # left not None -> продвигаемся left
        # left None -> продвигаемся right
        # left and right None -> возвращаем значение

        st = []
        ans = []

        while root or st:
            if root:
                st.append(root)
                root = root.left
            else :
                root = st.pop()
                ans.append(root.val)
                root = root.right

        return ans

        # st = 1 r=2 -> st= 1 2 r=None ->






s = Solution().inorderTraversal(one)
print(s)

# Рекурсия!


class Solution1:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


s = Solution1().inorderTraversal(one)
print(s)
