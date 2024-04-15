def find_common_numbers(lists):
    sets = [set(lst) for lst in lists]

    common = set()
    for i in range(3):
        for j in range(i+1, 3):
            common |= sets[i] & sets[j]

    return sorted(common)
spiski=[]
for i in range(3):
    n=int(input())
    digits = list(map(int, input().split()))
    spiski.append(digits)
print(*find_common_numbers(spiski))