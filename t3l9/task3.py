c = list(map(int, input().split()))
c1 = set()
for i in c:
    if i in c1:
        print(f"{i} YES")
    else:
        print(f"{i} NO")
        c1.add(i)


#  1 2 3 1 4 5 4 8 9