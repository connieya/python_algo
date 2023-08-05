import sys
import bisect

n, m = map(int, sys.stdin.readline().split())
arr = list( map(int, sys.stdin.readline().split()))
arr.sort()
for _ in range(m):
    s ,e = map(int, sys.stdin.readline().split())
    s_idx = bisect.bisect_left(arr , s)
    e_idx= bisect.bisect_right(arr,e)

    ans = e_idx-s_idx
    print(ans)