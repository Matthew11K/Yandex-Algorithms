n = int(input())
sectors = list(map(int, input().split()))
a, b, k = map(int, input().split())
if (b-a)//k>99999999:
    print(max(sectors))
else:
    if b%k==0:
        max_sectors = (b - 1) // k
    else:
        max_sectors = b//k

    if a%k==0:
        min_sectors = (a - 1) // k
    else:
        min_sectors = a//k
    best_win = 0

    for sectors_crossed in range(min_sectors, max_sectors + 1):
        for direction in [1, -1]:
            final_pos = (direction * sectors_crossed) % n
            best_win = max(best_win, sectors[final_pos])

    print(best_win)
