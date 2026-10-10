# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node):
                
            # base case
            if not node:
                return None

            # process curr node
            if max(p.val,q.val) < node.val:
                return dfs(node.left)
            # recursively expplore children
            elif min(p.val,q.val) > node.val:
                return dfs(node.right)
            else:
                return node

        # Turn result.
        return dfs(root)