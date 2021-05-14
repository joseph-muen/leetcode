# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

def traverse(root):
    current_level = [root]
    while current_level:
        print(' '.join(str(node) for node in current_level))
        next_level = list()
        for n in current_level:
            if n.left:
                next_level.append(n.left)
            if n.right:
                next_level.append(n.right)
            current_level = next_level


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def helper(x, y):
            if x > y: return [None]
            if x == y: return [TreeNode(x)]

            ans = []
            for v in range(x, y+1):
                lans = helper(x, v-1)
                rans = helper(v+1, y)

                for l in lans:
                    print(v,l)
                    # for r in rans:
                    #     print(v, l, r)
                    #     root = TreeNode(v)
                    #     root.left = l
                    #     root.right = r
                    #     ans.append(root)
            return ans
            # return lans, rans

        return helper(1, n) if n >= 1 else []
