from helpers.test import getOutcome
from collections import Counter

class Solution(object):
  def findLHS(self, nums):
    if len(nums) == 0:
      return 0
    counter = Counter(nums)
    sortedKeys = sorted(counter.keys())
    maxLength = 0
    prevKey = sortedKeys[0]
    for key in sortedKeys:
      currentCount = counter[key]
      if key - prevKey == 1:
        currentLength = currentCount + counter[prevKey]
        maxLength = currentLength if currentLength > maxLength else maxLength
      prevKey = key
    return maxLength

s = Solution()

getOutcome(
  [
    [1,3,2,2,5,2,3,7],
  ],
  [
    5,
  ],
  s.findLHS
)
