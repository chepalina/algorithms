# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        cache = dict()

        def iterate(left, right):
            if left == right:
                return [TreeNode(val=left)]
            if left > right:
                return [None]

            if cache.get((left, right)) is not None:
                return cache.get((left, right))

            res = []
            for val in range(left, right + 1):
                left_trees = iterate(left, val - 1)
                right_trees = iterate(val + 1, right)

                for left_tree in left_trees:
                    for right_tree in right_trees:
                        node = TreeNode(val, left_tree, right_tree)
                        res.append(node)

            cache[(left, right)] = res
            return res

        return iterate(1, n)
