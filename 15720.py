b, c, d = map(int, input().split())
bp = sorted(list(map(int, input().split())), reverse=True)
cp = sorted(list(map(int, input().split())), reverse=True)
dp = sorted(list(map(int, input().split())), reverse=True)
s = 0
for i in range(min(b, c, d)):
    s += (bp[i] + cp[i] + dp[i]) * 0.9
s += sum(bp[min(b, c, d)::]) + sum(cp[min(b, c, d)::]) + sum(dp[min(b, c, d)::])
print(sum(bp) + sum(cp) + sum(dp))
print(int(s))