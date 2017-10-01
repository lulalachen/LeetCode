class MapSum(object):
  def __init__(self):
    self.cache = {}

  def insert(self, key, val):
    self.cache[key] = val

  def sum(self, prefix):
    result = 0
    for key in self.cache.keys():
      if key.startswith(prefix):
        result += self.cache.get(key)
    return result


s = MapSum()
s.insert('apple', 3)
print(s.sum('app'))
s.insert('app', 2)
print(s.sum('app'))
