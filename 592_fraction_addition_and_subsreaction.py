from helpers.test import getOutcome

import re
from functools import reduce

def gcd(a, b):
  if a < b:
    a, b = b, a
  while b:
    a, b = b, a % b
  return a

def lcm(a, b):
  return int(a * b / gcd(a, b))

def mapWith(fn, iterable):
  return list(map(fn, iterable))

def addFractional(a, b):
  gcdOfTwo = gcd(a[1], b[1])
  return [a[0] * abs(b[1] / gcdOfTwo) + b[0] * abs(a[1] / gcdOfTwo), lcm(a[1], b[1])]

class Solution(object):
  def fractionAddition(self, expression):
    expression = '+' + expression
    nums = mapWith(
      lambda x: mapWith(int, x.split('/')),
      re.findall(r'[+|-]\d+\/\d+', expression)
    )
    numerator, denominator = reduce(
      addFractional,
      nums,
      [0, 1]
    )
    if numerator == 0:
      return "0/1"
    dividedBy = gcd(abs(numerator), abs(denominator))
    return '{}/{}'.format(str(int(numerator/dividedBy)), str(int(denominator/dividedBy)))

s = Solution()
test_input = [
  "-1/2+1/2",
  "-1/2+1/2+1/3",
  "1/3-1/2",
  "9/5-7/8+9/10+8/9-2/7-1/2+1/2+9/8-6/7+1/1"
]

expected_ourput = [
  "0/1",
  "1/3",
  "-1/6",
  "4657/1260"
]

getOutcome(test_input, expected_ourput, s.fractionAddition)
