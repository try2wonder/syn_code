st1 = input()
checkl = len(st1)//2
# print(checkl)
if st1[0:checkl] == st1[len(st1):(len(st1) - checkl - 1):-1]:
    print('yes')
else:
    print('no')
