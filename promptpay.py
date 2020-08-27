def basic():
    # input
    amt = 3000

    # process
    fee = 0
    if amt <= 5000:
        fee = 0
    elif amt > 5000 and amt <= 30000:
        fee = 2
    elif amt > 30000 and amt <= 100000:
        fee = 5
    else:
        fee = 10

    # output
    print("fee =", fee)


def basic2():
    amt = float(input("transfer amount:"))
    fee = 0
    if amt > 100000:
        fee = 10
    elif amt > 30000:
        fee = 5
    elif amt > 5000:
        fee = 2
    else:
        fee = 0

        print("fee =", fee)

if __import__=='_main_':
    basic2()
