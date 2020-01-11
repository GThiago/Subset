def ArrayAdditionI(arr, res):
  if len(arr) == 0:
    return False
  elif arr[0] == res:
    return True
  else:
    return ArrayAdditionI(arr[1:], res-arr[0]) or ArrayAdditionI(arr[1:],res)
  
def aux(arr):
  aux = []
  for n in arr:
    aux1 = arr
    for i in aux1:
      if (i != n):
        aux.append(i)
    if ArrayAdditionI(aux,n):
      return True
    aux = []
  return False

print(aux(input()))
