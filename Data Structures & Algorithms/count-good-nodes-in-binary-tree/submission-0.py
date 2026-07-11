# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(curr, maxVal):
            if not curr:
                return 0
            
            res = 1 if maxVal <= curr.val else 0
            maxVal = max(maxVal, curr.val)
            res += dfs(curr.left, maxVal)
            res += dfs(curr.right, maxVal)
            return res

        return dfs(root, root.val)
        