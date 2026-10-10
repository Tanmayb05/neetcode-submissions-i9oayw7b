# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        output = []
        def dfs(node):
            nonlocal k, output
            if not node: return None
            dfs(node.left)
            if k>0:
                output.append(node.val)
                k-=1
            else:
                return
            dfs(node.right)
        dfs(root)
        return output[-1]
        # return output[k-1]