from helpers.Tree import Tree

class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution(object):
  def tree2str(self, t, isLeft=False):
    if t is None:
      return ''
    if t.left is not None and t.right is not None:
      return '{}({left})({right})'.format(
        str(t.val),
        left=self.tree2str(t.left, True),
        right=self.tree2str(t.right, False)
      )
    elif t.left is not None and t.right is None:
      return '{}({left})'.format(
        str(t.val),
        left=self.tree2str(t.left, True)
      )
    elif t.left is None and t.right is not None:
      return '{}()({right})'.format(
        str(t.val),
        right=self.tree2str(t.right, False)
      )
    else:
      return str(t.val)

s = Solution()
tree = Tree([1,2,3,None,4])
root = tree.root
print(root.val, root.right.val, root.left.val)
