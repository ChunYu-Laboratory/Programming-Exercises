def f(num):
  count = 1 # self
  for i in reverse(range(1, num)):
    count += f(i) # (num - i, i), recursive calculate i
  return count
