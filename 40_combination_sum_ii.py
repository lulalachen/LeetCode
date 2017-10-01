from helpers.test import getOutcome

class Solution:
  def combinationSum2(self, candidates, target):
    candidates.sort()
    return self.search(candidates, 0 ,target)

  def search(self, candidates, start, target):
    if target == 0:
      return [[]]
    res = []
    for i in range(start,len(candidates)):
      if i != start and candidates[i] == candidates[i-1]:
        continue
      if candidates[i] > target:
        break
      for r in self.search(candidates, i+1, target-candidates[i]):
        res.append([candidates[i]]+r)
    return res

s = Solution()
res = s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
print(res)
