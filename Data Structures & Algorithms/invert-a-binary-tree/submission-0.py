# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root

        def preorder(curr):
            if not curr:
                return None
            
            original_left = curr.left
            original_right = curr.right
            
            curr.left = preorder(original_right)
            curr.right = preorder(original_left)

            return curr

        preorder(root)
        return root