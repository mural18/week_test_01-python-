def getMaxProfit(pnl, k):
    ans = float("-inf")

    n = len(pnl)

    for i in range(n):
        total = 0

        for j in range(i, min(i + k, n)):
            total += pnl[j]

            if total > ans:
                ans = total

    return ans


n = int(input())

pnl = []

for i in range(n):
    pnl.append(int(input()))

k = int(input())

print(getMaxProfit(pnl, k))