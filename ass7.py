amt = int(input("enter amount:"))
str = int(input("enter denominations:"))
denominations = [100, 50, 20, 10, 5, 2, 1]
match str:
    case 100:
        idx = 0
    case 50:
        idx = 1
    case 20:
        idx = 2
    case 10:
        idx = 3
    case 5:
        idx = 4
    case 2:
        idx = 5
    case 1:
        idx = 6
    case _:
        print("Invalid denomination")
        exit()


for i in range(idx, len(denominations)):
    note = denominations[i]
    count = amt // note
    amt %= note
    print(f"{note} rupees note: {count}")