from helpers.test import getOutcome
from datetime import datetime, timedelta

class Solution(object):
  timeFormat = '%H:%M'

  def getTimeStrSet(self, timeStr):
    return set(list(timeStr.replace(':', '')))

  def stringifyTime(self, time):
    return datetime.strftime(time, self.timeFormat)

  def parseIntoTime(self, timeStr):
    return datetime.strptime(timeStr, self.timeFormat)

  def isTimeDigitsAvailable(self, time):
    timeStr = self.stringifyTime(time)
    currentTimeDigitSet = self.getTimeStrSet(timeStr)
    if currentTimeDigitSet.issubset(self.timeDigitSet):
      return True
    else:
      return False

  def nextClosestTime(self, time):
    self.timeDigitSet = self.getTimeStrSet(time)
    baseTime = self.parseIntoTime(time)

    for delta in range(1, 60 * 24 + 1):
      time = baseTime + timedelta(minutes=delta)
      if self.isTimeDigitsAvailable(time):
        return self.stringifyTime(time)


s = Solution()

test_inputs = [
  "19:34",
  "23:59",
]

expected_outputs = [
  "19:39",
  "22:22",
]

getOutcome(test_inputs, expected_outputs, s.nextClosestTime)
