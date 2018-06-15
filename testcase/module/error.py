
def run():
  n=10
  sum1=0
  for i in range(1,n+1):
      sum1=sum1+(1/i)
  assert(i == 11), "gg"
  print("The sum of series is",round(sum1,2))