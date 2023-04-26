def problem1(n):
    i = 0
    ans = 0
    while (i < n):
        i+=1
        if (i%3==0 or i%5==0 and not (i%15==0)):
            ans+=i
        elif (i%15):
            ans+=i/2
    return ans
print(problem1(1000))
