a = int(input())
cnt = 0
if a <= 2e9:
    for i in range(1, a + 1):
        if a % i == 0:
            cnt += 1
            print ('i==', i)
    print(cnt)
else:
    print("the number is bigger than 2e9")