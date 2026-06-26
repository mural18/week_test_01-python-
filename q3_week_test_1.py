password = input()
balance = int(input())

q = int(input())

state = "unauthorized"

for _ in range(q):

    data = input().split()
    action = data[0]

    if action == "login":
        if state == "unauthorized" and data[1] == password:
            state = "authorized"
            print("Success=True", state)
        else:
            print("Success=False", state)

    elif action == "logout":
        if state == "authorized":
            state = "unauthorized"
            print("Success=True", state)
        else:
            print("Success=False", state)

    elif action == "deposit":
        if state == "authorized":
            balance += int(data[1])
            print("Success=True", state)
        else:
            print("Success=False", state)

    elif action == "withdraw":
        if state == "authorized" and balance >= int(data[1]):
            balance -= int(data[1])
            print("Success=True", state)
        else:
            print("Success=False", state)

    elif action == "balance":
        if state == "authorized":
            print("Success=True", state, balance)
        else:
            print("Success=False", state)