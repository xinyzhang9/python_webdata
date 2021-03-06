# Given a binary tree, find the maximum path sum.

# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path does not need to go through the root.

# For example:
# Given the below binary tree,

#        1
#       / \
#      2   3
# Return 6.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxSum,_ = self.helper(root)
        return maxSum
    
    def helper(self,root):
        if root is None:
            return -sys.maxint,0
        left = self.helper(root.left)
        right = self.helper(root.right)
        # left part, right part or cross the root
        maxPath = max(left[0],right[0],root.val + left[1]+right[1])
        # may discard negative sum
        single = max(left[1]+root.val,right[1]+root.val,0)
        return maxPath,single