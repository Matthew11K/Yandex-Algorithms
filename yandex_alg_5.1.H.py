PI = 3.141592653589793
def calculate_time_to_meet(L, x1, v1, x2, v2):
    if v1 == v2 == 0 and not (x1 + x2 == L or x1 == x2):
        return "NO", None
    if x1==x2 or (v1 == v2 == 0 and (x1 + x2 == L or x1 == x2)):
        return "YES", 0
    if v1 == v2 and x1 != x2:
        if v1 > 0:
            return "YES", ((2 * L - x1 - x2) % L) / (v1 + v2)
        elif v1 < 0:
            return "YES", ((abs(x1) + abs(x2)) / (2 * abs(v1)))
    if (v1 < 0 and v2 < 0) or (v1 == 0 and v2 < 0) or (v2 == 0 and v1 < 0):
        return "YES", -((x1 + x2 - (2 * L)) % L) / (v1 + v2)

    pos1 = (x1 / L) * 2 * PI
    pos2 = (x2 / L) * 2 * PI
    w1 = (2 * PI * v1) / L
    w2 = (2 * PI * v2) / L

    t = float("inf")
    best_time=float("inf")
    k=-99
    while k!=99:
        cur_time=(2 * PI * k + pos2 - pos1) / (w1 - w2)
        if abs(v1) != abs(v2):
            t = (2 * L - x1 - x2) % L / (v1 + v2)
        if cur_time>0:
            time = min(cur_time, t)
        else:
            time=t
        if best_time>time:
            best_time = time
        k+=1
    return "YES", best_time


L, x1, v1, x2, v2 = map(int, input().split())
answer, time = calculate_time_to_meet(L, x1, v1, x2, v2)
print(answer)
if answer == "YES":
    print(f"{time:.10f}")