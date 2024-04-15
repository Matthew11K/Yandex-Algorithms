t=int(input())
for _ in range(t):
    n=int(input())
    numbers=list(map(int,input().split()))
    answLen=[]
    cnt=1
    minNow=numbers[0]
    for i in range(1,n):
        minNow = min(minNow, numbers[i])
        if minNow<cnt+1:
            answLen.append(cnt)
            cnt=0
            minNow = numbers[i]
        cnt += 1
    if cnt != 0:
        answLen.append(cnt)
    print(len(answLen))
    print(*answLen)