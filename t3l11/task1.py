def tmp(n):
    fac = 1
    facl = [1]
    for i in range(2,n+1):
        fac *= i
        facl.append(fac)
    facl.reverse()
    print(facl)
    

tmp(int(input()))

