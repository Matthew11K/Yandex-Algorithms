n=int(input())
lengths=list(map(int,input().split()))

s=sum(lengths)
m=max(lengths)
if s<2*m:
    print(2*m-s)
else:
    print(s)