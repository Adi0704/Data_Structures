from collections import deque
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def bfs(root):
    if not root:
        return []
    print("Root:",root)

    q=deque([root])
    print(q[0].val)
    res=[]
    while q:
        print(q)
        node=q.popleft()
        print(node.val,end=" ")
        res.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return res
# constructing the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print(bfs(root))