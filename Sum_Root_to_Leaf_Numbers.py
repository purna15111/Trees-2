# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.final = []
        def inorder(main,num):
            num *= 10
            num += main.val
            
            if main.left is None and main.right is None:
                self.final.append(num)
                return
            if main.left is not None:
                inorder(main.left,num)
            if main.right is not None:
                inorder(main.right,num)
        inorder(root,0)
        print(self.final)
        return sum(self.final)