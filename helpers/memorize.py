def memorize(fn):
  cacheStore = dict()
  def memorizedFn(*argv):
    key = str(argv)
    cache = cacheStore.get(key)
    if cache:
      return cache
    else:
      calculation = fn(*argv)
      cacheStore[key] = calculation
      return calculation
  return memorizedFn
