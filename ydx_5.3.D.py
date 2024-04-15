def has_repeats_within_k(n, k, sequence):
    last_indexes = {}

    for i, num in enumerate(sequence):
        if num in last_indexes and i - last_indexes[num] <= k:
            return "YES"
        last_indexes[num] = i

    return "NO"
n,k=list(map(int,input().split()))
digits=list(map(int,input().split()))
print(has_repeats_within_k(n,k,digits))