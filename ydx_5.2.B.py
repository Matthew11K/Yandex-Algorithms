n,k = map(int,input().split())
prices = list(map(int,input().split()))
earned = 0
canEarn=0
for i in range(n):
    for j in range(i+1,i+k+1):
        if j<n:
            if prices[j]-prices[i]>canEarn:
                canEarn=prices[j]-prices[i]
    if canEarn>earned:
        earned=canEarn
print(earned)