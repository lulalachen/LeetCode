from helpers.test import getOutcome

class Solution(object):
  def numberOfBoomerangs(self, points):
    result = 0
    for p1 in points:
      cache = {}
      for p2 in points:
        dx = p1[0] - p2[0]
        dy = p1[1] - p2[1]
        cache[dx**2 + dy**2] = 1 + cache.get(dx**2 + dy**2, 0)
      for k in cache:
        result += cache[k] * (cache[k] -1)
    return result


s = Solution()

test_inputs = [
  [ [0,0], [1,0], [2,0], [-1,0] ],
]

expected_outputs = [
  4,
]

getOutcome(test_inputs, expected_outputs, s.numberOfBoomerangs)
