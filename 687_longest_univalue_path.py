from helpers.Tree import Tree
from helpers.test import getOutcome
from itertools import combinations

class Solution(object):
  def traverse(self, node, path):
    self.treeNodePositions.setdefault(node.val, [])
    self.treeNodePositions.get(node.val).append(path)

    if node.left is not None:
      leftIndex = path[-1] * 2
      self.traverse(node.left, path + [leftIndex])
    if node.right is not None:
      rightIndex = path[-1] * 2 + 1
      self.traverse(node.right, path + [rightIndex])

  def longestUnivaluePath(self, root):
    if root is None:
      return 0
    self.treeNodePositions = dict()
    self.traverse(root, [1])
    lengths = set({0})
    for value, paths in self.treeNodePositions.items():
      if len(paths) >= 2:
        for a, b in list(combinations(paths, 2)):
          setA = set(a)
          setB = set(b)
          print(value, paths, a, b, len((setA | setB) - (setA & setB)))
          lengths.add(len((setA | setB) - (setA & setB)))
    return max(lengths)

s = Solution()

tree1 = Tree([1])
tree2 = Tree([5,4,5,1,1,5])
tree3 = Tree([1,2,2,2,2])
inputs = [
  tree1.root,
  tree2.root,
  tree3.root,
]

expected_output = [
  0,
  2,
  2,
]

getOutcome(inputs, expected_output, s.longestUnivaluePath)
