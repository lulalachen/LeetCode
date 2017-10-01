class Solution(object):
  def findRestaurant(self, list1, list2):
    idx_a = {}
    idx_b = {}
    for idx, val in enumerate(list1):
      idx_a[val] = idx
    for idx, val in enumerate(list2):
      idx_b[val] = idx
    intersects = set(idx_a).intersection((set(idx_b)))
    min = float('Inf')
    restaurant = []
    for key in intersects:
      sums = idx_a[key] + idx_b[key]
      if sums < min:
        min = sums
        restaurant = [key]
      elif sums == min:
        restaurant.append(key)
    return restaurant
