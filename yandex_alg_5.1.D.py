table = [[0 for _ in range(8)] for _ in range(8)]

for i in range(8):
    a = input()
    for j in range(8):
        table[i][j] = a[j]

def mark_rook_attacks(x, y):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in directions:
        i, j = x, y
        while 0 <= i < 8 and 0 <= j < 8:
            if (i != x or j != y) and (table[i][j] == 'R' or table[i][j] == 'B'):
                break
            if table[i][j] == '*':
                table[i][j] = 'L'
            i, j = i + dx, j + dy


def mark_bishop_attacks(x, y):
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dx, dy in directions:
        i, j = x, y
        while 0 <= i < 8 and 0 <= j < 8:
            if (i != x or j != y) and (table[i][j] == 'R' or table[i][j] == 'B'):
                break
            if table[i][j] == '*':
                table[i][j] = 'S'
            i, j = i + dx, j + dy

for i in range(8):
    for j in range(8):
        if table[i][j] == 'R':
            mark_rook_attacks(i, j)
        elif table[i][j] == 'B':
            mark_bishop_attacks(i, j)

cnt = sum(row.count('*') for row in table)
print(cnt)
for i in range(8):
    print(*table[i])