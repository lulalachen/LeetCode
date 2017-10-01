from helpers.test import getOutcome

class Solution(object):
  def findMaxConsecutiveOnes(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    maxLength = 0
    flag = False
    temp = 0
    for n in nums:
      if flag == False and n == 1:
        flag = True
        temp += 1
      elif flag == True and n == 1:
        temp += 1
      else:
        maxLength = temp if temp > maxLength else maxLength
        flag = False
        temp = 0
    maxLength = temp if temp > maxLength else maxLength
    return maxLength

s = Solution()

test_inputs = [
  [1],
  [1,0,1,1,0,1],
  [1,1,1,1,0,0,0,1,1],
  [1,0,1,1,0,0,0,1,1],
]

expected_outputs = [
  1,
  2,
  4,
  2,
]

getOutcome(test_inputs, expected_outputs, s.findMaxConsecutiveOnes)
