from helpers.test import getOutcome

class Solution(object):
  def findRedundantConnection(self, edges):

    return


s = Solution()

test_inputs = [
  [[1,2], [1,3], [2,3]],
  [[1,2], [1,3], [3,1]],
  [[9,1],[2,10],[2,6],[8,7],[5,7],[8,9],[2,4],[3,7],[1,5],[4,7]],
]

expected_outputs = [
  [2, 3],
  [3, 1],
  [1, 5],
]

getOutcome(test_inputs, expected_outputs, s.findRedundantConnection)
