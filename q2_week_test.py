def countDuplicates(name, price, weight):
    seen = set()
    count = 0

    for i in range(len(name)):
        product = (name[i], price[i], weight[i])

        if product in seen:
            count += 1
        else:
            seen.add(product)

    return count


n = int(input())
name = [input() for _ in range(n)]

n = int(input())
price = [int(input()) for _ in range(n)]

n = int(input())
weight = [int(input()) for _ in range(n)]

print(countDuplicates(name, price, weight))