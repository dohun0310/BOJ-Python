try:
    n = int(input())
    l = list(map(int, input().split()))
    g = list(map(int, input().split()))
    t = 0
    for i in range(n - 1):
        if t >= l[i]:
            t = max(t, l[i] + g[i])
    if t >= l[n - 1]:
        print("권병장님, 중대장님이 찾으십니다")
    else:
        print("엄마 나 전역 늦어질 것 같아")
except:
    print("권병장님, 중대장님이 찾으십니다")