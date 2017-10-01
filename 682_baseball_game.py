from helpers.test import getOutcome

class Solution(object):
  temp = []
  def addIntoTemp(self, point):
    if len(self.temp) == 4:
      self.temp = self.temp[1:4] + [point]
    else:
      self.temp.append(point)

  def removeLastFromTemp(self):
    if len(self.temp) == 4:
      self.temp = [0] + self.temp[0:3]
    else:
      self.temp.pop()

  def calPoints(self, ops):
    result = 0
    for opOrPoints in ops:
      try:
        point = int(opOrPoints)
        result += point
        self.addIntoTemp(point)
      except Exception as e:
        if opOrPoints == 'D':
          doubledPoints = 2 * self.temp[-1]
          result += doubledPoints
          self.addIntoTemp(doubledPoints)
        elif opOrPoints == 'C':
          removedPoints = self.temp[-1]
          result -= removedPoints
          self.removeLastFromTemp()
        elif opOrPoints == '+':
          sumedPoints = sum(self.temp[-2:])
          result += sumedPoints
          self.addIntoTemp(sumedPoints)
    return result




s = Solution()

test_inputs = [
  ["5","2","C","D","+"],
  ["5","-2","4","C","D","9","+","+"],
  ["-24711","1638","-14561","22699","+","-14761","+","-12508","-6212","21079","28567","+","-10608","D","C","C","-13729","10966","16247","-12579","-23765","C","-1549","+","+","24480","29791","25860","22932","13079","-2975","C","D","18681","C","-5938","D","-23912","C","-29207","D","15594","-2524","20105","9269","C","-2239","6133","+","27432","-28272","D","-23433","C","3698","24623","20802","-1753","-28396","25669","D","29729","C","C","C","1069","D","C","11031","16678","+","D","+","-5961","-10969","21949","-16741","-17685","-9050","-6234","+","+","C","223","28138","-1233","C","D","-11570","-15341","D","+","-1097","14092","+","-26148","18620","-28131","C","-21594"],
]

expected_outputs = [
  30,
  27,
  174306,
]

getOutcome(test_inputs, expected_outputs, s.calPoints)
