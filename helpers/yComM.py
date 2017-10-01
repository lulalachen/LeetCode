def yComM(genFn, cacheStore = dict()):
  def memorizedFn(*argv):
    key = str(argv)
    if cacheStore.get(key):
      return cacheStore.get(key)
    else:
      calculation = yComM(genFn, cacheStore)(*argv)
      cacheStore[key] = calculation
      return calculation
  return genFn(memorizedFn)
