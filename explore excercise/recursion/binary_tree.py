# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        current_depth = left_depth = right_depth = 1
        def helper(root, left_depth, right_depth, current_depth):
            if root.left != None:
                left_depth = helper(root.left, left_depth, right_depth, current_depth + 1)
            if root.right != None:
                right_depth = helper(root.right, left_depth, right_depth, current_depth + 1)
            if root.left == None and root.right == None:
                current_depth = current_depth
            return max(left_depth, right_depth, current_depth)
        if not root:
            return 0
        else:
            return helper(root, left_depth, right_depth, current_depth)
