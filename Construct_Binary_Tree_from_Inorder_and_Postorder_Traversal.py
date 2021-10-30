# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0 and len(postorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        
        def treebuilder(inorder,postorder):
            if len(inorder) == 0 and len(postorder) == 0:
                return
            temp = TreeNode(postorder[-1])
            
            ino_left = inorder[:inorder.index(postorder[-1])]
            ino_right = inorder[inorder.index(postorder[-1])+1:]
            
            post_left = postorder[:len(ino_left)]
            post_right = postorder[len(ino_left):-1]
            
            temp.left = treebuilder(ino_left,post_left)
            temp.right = treebuilder(ino_right,post_right)
            return temp
            
        ino_left = inorder[:inorder.index(postorder[-1])]
        ino_right = inorder[inorder.index(postorder[-1])+1:]
        
        post_left = postorder[:len(ino_left)]
        post_right = postorder[len(ino_left):-1]
        
        root.left = treebuilder(ino_left,post_left)
        root.right = treebuilder(ino_right,post_right)
        
        print(ino_left,ino_right,post_left,post_right)
        return root