from helpers.test import getOutcome

from math import ceil

class Solution(object):
  def validPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    if s == s[::-1]:
      return True
    s = 'a' + s + 'a'
    length = len(s)

    for idx in range(0, length // 2):
      negIdx = -(idx+1)
      if s[idx] == s[negIdx]:
        continue
      else:
        correctLeft = s[idx+1:negIdx+1]
        correctRight = s[idx:negIdx]
        # negIdx = None if None == -1 else negIdx
        # print(idx, negIdx, s[idx], s[negIdx], correctLeft, correctRight)
        if len(correctLeft) == 1 and len(correctRight) == 1:
          return True

        return correctLeft == correctLeft[::-1] or correctRight == correctRight[::-1]
    return Ture

s = Solution()
inputs = [
  'abc',
  'abca',
  'abcba',
  'abcdcbda',
  'deeee',
  'eeeed',
  'acbbba',
  'ebcbbececabbacecbbcbe',
]
expected_outcome = [
  False, True ,True ,True ,True ,True ,True ,True
]
getOutcome(inputs, expected_outcome, s.validPalindrome)
