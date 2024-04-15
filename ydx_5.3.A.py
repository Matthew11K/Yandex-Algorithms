def find_common_tracks():
    n = int(input())
    common_tracks = None

    for _ in range(n):
        k = int(input())
        tracks = set(input().split())

        if common_tracks is None:
            common_tracks = tracks
        else:
            common_tracks &= tracks

    if common_tracks:
        common_tracks = sorted(common_tracks)
        print(len(common_tracks))
        print(' '.join(common_tracks))
    else:
        print(0)

find_common_tracks()
