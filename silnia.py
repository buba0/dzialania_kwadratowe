def silnia(n):
    if n == 1:
        return 1
    else:
        return n * silnia(n-1)
    
n = 4
print(silnia(n))