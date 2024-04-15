n=int(input())
coordinates=[]
for i in range(n):
    coordinates.append(list(map(int,input().split())))
directions=[(1,0), (-1,0), (0,1), (0,-1)]
perim=0
for kr in coordinates:
    maxSights=4
    x = kr[0]
    y = kr[1]
    for dx,dy in directions:
        i,j = x,y
        i, j = i + dx, j + dy
        if list((i,j)) in coordinates:
            if maxSights > 0:
                maxSights-=1
    perim+=maxSights
print(perim)