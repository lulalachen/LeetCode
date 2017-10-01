from helpers.test import getOutcome

previousPaths = 0
currentPaths = 1
cache = {
  "0": 0,
  "1": 1,
}
def fib(n):
  cachedValue = cache.get(str(n))
  if cachedValue is not None:
    return cachedValue
  else:
    temp = fib(n-1) + fib(n-2)
    cache[str(n)] = temp
    return temp

class Solution(object):
  def climbStairs(self, n):
    return fib(n)

s = Solution()
test_input = [4, 5, 6, 100]
expect_output = [3, 5, 8, 354224848179261915075]
getOutcome(test_input, expect_output, s.climbStairs)
