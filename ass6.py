def reverse_num(n):
    return int(str(n)[::-1])   

test = int(input("Enter number of test cases:"))               
for _ in range(test):
    a, b = input().split()    
    rev_a = reverse_num(a)      
    rev_b = reverse_num(b)    
    total = rev_a + rev_b      
    result = reverse_num(total)
    print(result)