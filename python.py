cache = [0, 1, 1] + [None for i in range(10)]
#print(cache)

def FBI(n):
  if cache[n]:
    return cache[n]
  cache[n] = FBI(n-1) + FBI(n-2)
  #print(cache)
  return cache[n]


print(FBI(25))