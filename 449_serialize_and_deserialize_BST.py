# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

def get(array, index):
  try:
    return array[index]
  except:
    return None

class Codec:
  def destructTree(self, node, result):
    leftNode = node.left
    rightNode = node.right

    currentValue = node.val
    leftValue = leftNode.val
    rightValue = rightNode.val

    result.append(currentValue)
    if leftNode is not None:
      result.append(self.destructTree(), )


  def serialize(self, root):
    """Encodes a tree to a single string.

    :type root: TreeNode
    :rtype: str
    """
    currentIndex = 1
    result = []
    serializedTree = self.destructTree(root, result)

  def constructTree(self, index):
    currentValue = get(self.unserializedTree, index)

    leftIndex = 2 * index
    rightIndex = 2 * index + 1
    leftValue = get(self.unserializedTree, leftIndex)
    rightValue = get(self.unserializedTree, rightIndex)

    currentNode = TreeNode(currentValue)
    currentNode.left = None if leftValue is None else self.constructTree(leftIndex)
    currentNode.right = None if rightValue is None else self.constructTree(rightIndex)

    return currentNode

  def deserialize(self, data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """
    self.unserializedTree = [None] + data.replace('[', '').replace(']', '').split(',')
    print (self.unserializedTree)
    rootNode = self.constructTree(1)

    return rootNode

# Your Codec object will be instantiated and called as such:
codec = Codec()
arr_str = "[2,1,3,4,5,7,9]"
print(codec.deserialize(arr_str))
print(codec.serialize(codec.deserialize(arr_str)))
