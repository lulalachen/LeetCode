from helpers.test import getOutcome

from functools import reduce

def orOperator(f, g):
  return f or g

def any(*args):
  return reduce(orOperator, args)

class Solution(object):
  def checkValidString(self, s):
    self.rawString = s
    self.rawStringLength = len(s)
    return self.dfs(0, 0)

  def dfs(self, currentIndex, leftParenthesisCount):
    if currentIndex == self.rawStringLength:
      return leftParenthesisCount == 0
    if leftParenthesisCount < 0:
      return False

    if self.rawString[currentIndex] == '(':
      return self.dfs(currentIndex + 1, leftParenthesisCount + 1)
    elif self.rawString[currentIndex] == ')':
      return self.dfs(currentIndex + 1, leftParenthesisCount - 1)
    else:
      return any(
        self.dfs(currentIndex + 1, leftParenthesisCount - 1),
        self.dfs(currentIndex + 1, leftParenthesisCount + 1),
        self.dfs(currentIndex + 1, leftParenthesisCount),
      )


s = Solution()
inputs = [
  '(())',
  '(*))',
  '*())',
  '*()))',
  '(()(())()())*((()(())))*()(*)()()(*((()((*(*))))()*()(()((()(*((()))*(((())(())))*))(()*))(()*)'
]

expected_output = [
  True,
  True,
  True,
  False,
  True,
]

getOutcome(inputs, expected_output, s.checkValidString)
