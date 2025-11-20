import math

a = int(input("enter number of test cases:"))

for _ in range(a):
    X, Y = map(int, input().split())
    
    gcd = math.gcd(X, Y)
    lcm = (X * Y) // gcd   
    
    print("Greatest common divisor and Least common factor:",gcd,",", lcm)