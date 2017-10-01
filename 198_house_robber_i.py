from helpers.test import getOutcome

class Solution(object):
  cache = {
    0: 0,
  }

  def fib(self, n):
    index = n - 1
    print(n)
    if n == self.numsLength:
      return self.cache.get(index)
    elif n == 1:
      self.cache[1] = self.nums[index]
      return self.cache[1]
    elif n == 2:
      self.cache[2] = max(self.nums[0], self.nums[1])
      return self.cache[2]
    else:
      idx = n - 1
      self.cache[n+2] = max(self.fib(n+1), self.fib(n) + self.nums[idx])
      return self.cache[n+2]

  def rob(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    self.nums = nums
    self.numsLength = len(nums)
    print (self.fib(1))
    print (self.cache)
    return self.fib(1)

s = Solution()

test_input = [
  [100, 5, 7, 70, 80, 90],
  [1, 2, 3, 4],
]

expected_output = [
  [100, 5, 7, 102],
  [1, 2, 3, 4],
]

getOutcome(test_input, expected_output, s.rob)
