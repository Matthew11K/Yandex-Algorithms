def count_paintable_trees(P, V, Q, M):
    min_vasya = P - V
    max_vasya = P + V
    min_masha = Q - M
    max_masha = Q + M

    if max_vasya < min_masha or max_masha < min_vasya:
        vasya_trees = V * 2 + 1
        masha_trees = M * 2 + 1
        return vasya_trees + masha_trees

    common_min = max(min_vasya, min_masha)
    common_max = min(max_vasya, max_masha)

    total_paintable = common_max - common_min + 1

    if min_vasya < common_min:
        total_paintable += common_min - min_vasya
    if max_vasya > common_max:
        total_paintable += max_vasya - common_max
    if min_masha < common_min:
        total_paintable += common_min - min_masha
    if max_masha > common_max:
        total_paintable += max_masha - common_max

    return total_paintable

P, V = map(int, input().split())
Q, M = map(int, input().split())

print(count_paintable_trees(P, V, Q, M))
