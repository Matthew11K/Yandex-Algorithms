k=int(input())
coordinates=[]
for i in range(k):
    coordinates.append(input().split())
cur_min_x=10**9 + 1
cur_max_x=int(coordinates[0][0])
cur_min_y=10**9 + 1
cur_max_y=int(coordinates[0][0])
for kr in coordinates:
    if int(kr[0])>cur_max_x:
        cur_max_x=int(kr[0])
    if int(kr[1])>cur_max_y:
        cur_max_y=int(kr[1])
    if int(kr[0])<cur_min_x:
        cur_min_x=int(kr[0])
    if int(kr[1])<cur_min_y:
        cur_min_y=int(kr[1])
print(cur_min_x,cur_min_y,cur_max_x,cur_max_y)
