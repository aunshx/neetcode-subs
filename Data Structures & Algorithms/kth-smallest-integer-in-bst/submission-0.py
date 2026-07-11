# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        max_heap = []

        def dfs(root):
            if not root:
                return

            heapq.heappush(max_heap,-root.val)
            if root.left:
                dfs(root.left)
            if len(max_heap) > k:
                heapq.heappop(max_heap)
            if root.right:
                dfs(root.right)
            
        dfs(root)
        return -1 if not len(max_heap) else -max_heap[0]
        