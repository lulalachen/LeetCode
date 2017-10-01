from helpers.test import getOutcome

class Solution(object):
  def sumDigitSquare(self, n):
    if n < 10:
        return n * n
    last_digit, remain = n % 10, n // 10
    return self.sumDigitSquare(remain) + last_digit * last_digit

  def intoKey(self, n):
    return ','.join(sorted(str(n)))

  def isHappy(self, n):
    self.checked = []
    current = n
    currentKey = self.intoKey(n)

    while currentKey not in self.checked:
      self.checked.append(self.intoKey(current))
      current = self.sumDigitSquare(current)
      currentKey = self.intoKey(current)
      if current == 1:
        return True
    return False

s = Solution()

test_inputs = [
  19,
  31,
  30,
]

expected_outputs = [
  True,
  True,
  False,
]

getOutcome(test_inputs, expected_outputs, s.isHappy)
