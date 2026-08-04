# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root1, root2):
            if not root1 and not root2:
                return True
            elif root1 and root2 and root1.val == root2.val:
                return sameTree(root1.left, root2.left) and sameTree(root1.right, root2.right)
            else:
                return False
        def dfs(curr):
            if not curr:
                return False
            if sameTree(curr, subRoot):
                return True
            elif dfs(curr.right) or dfs(curr.left):
                return True
            return False
            
            dfs(curr.right)
            dfs(curr.left)
        return dfs(root)
            


