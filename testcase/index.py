n=10
sum1=0
a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(1,n+1):
    sum1=sum1+(1/i)
    a[i] = sum1
print("The sum of series is",round(sum1,2))