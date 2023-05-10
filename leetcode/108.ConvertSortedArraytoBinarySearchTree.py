# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        if not nums:
            return None

        left = 0
        right = len(nums)

        middle = (left + right) //2

        left_node=self.sortedArrayToBST(nums[0:middle])
        right_node=self.sortedArrayToBST(nums[middle+1:right])

        return TreeNode(nums[middle],left_node,right_node)

