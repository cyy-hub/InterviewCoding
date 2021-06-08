# 自顶向下
class Solution():
    def __init__(self):
        self.res
    def tree_high(self,root)
        def tree_high_top_down(node,l):
            if node == None:
                return 
            if node.left == None and node.right== None:
                self.res = max(self.res, l)
            self.tree_high(node.left,l+1)
            self.tree_high(node.right,l+1)
        def tree_high_button_up(node):
            if node == None:
                return 0
            left = tree_high_button_up(node.left)
            right = tree_high_button_up(node.rigth)
            return max(left, right) +1
        tree_high_top_down(root,1)
        hight2=tree_high_button_up(root)
        print(self.res,hight2)