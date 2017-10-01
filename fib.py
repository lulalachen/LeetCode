from helpers.test import getOutcome
from helpers.yComM import yComM

def genFib(fn):
  def fib(n):
    if n == 1 or n == 2:
      return 1
    else:
      return fn(n - 1) + fn(n - 2)
  return fib

fib = yComM(genFib)

getOutcome(
  [100, 150],
  [354224848179261915075, 9969216677189303386214405760200],
  fib,
)
