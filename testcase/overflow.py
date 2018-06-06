n=10
sum1=0
for i in range(1,n+1):
    sum1=sum1+(1/i)
    k = 256
    a = (4. / (8. * k + 1.) - 2. / (8. * k + 4.) - 1. / (8. * k + 5.) - 1. / (8. * k + 6.)) / 16. ** k
print("The sum of series is",round(sum1,2))