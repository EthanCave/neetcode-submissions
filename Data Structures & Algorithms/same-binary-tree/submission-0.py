# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def isEquivalent(tree1,tree2):
            print(tree1, tree2)
            if not tree1 and not tree2:
                return True
            if not tree2 or not tree1:
                return False
            if tree1.val != tree2.val:
                return False
            if tree1.val == tree2.val:
                left = isEquivalent(tree1.left, tree2.left)
                right = isEquivalent(tree1.right, tree2.right)
            return left and right
        return isEquivalent(p,q)
            


