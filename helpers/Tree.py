class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Tree(object):
  def __init__(self, arrayOfNodes):
    self.root = self.deserialize(arrayOfNodes)

  def get(self, index):
    try:
      return self.unserializedTree[index]
    except:
      return None

  def constructTree(self, index):
    currentValue = self.get(index)

    leftIndex = 2 * index
    rightIndex = 2 * index + 1
    leftValue = self.get(leftIndex)
    rightValue = self.get(rightIndex)

    currentNode = TreeNode(currentValue)
    currentNode.left = None if leftValue is None else self.constructTree(leftIndex)
    currentNode.right = None if rightValue is None else self.constructTree(rightIndex)

    return currentNode

  def deserialize(self, data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """
    self.serializedTree = data
    self.unserializedTree = [None] + data
    rootNode = self.constructTree(1)

    return rootNode
