a = int(input("enter number of itearations"))
b = 0

for i in range(a):
    c = int(input("Enter the base value: "))
    d = int(input("Enter power: "))
    b = (pow(c,d)) % 10
    print(b)