n1 = int(input())
# 1 2 3 4 5 6
arr = list(map(int,input().split()))
# Ограничим введённый массив до n1 элементов
arr1 = arr[:n1]
x = arr1.pop()
arr1.insert(0, x)
print(arr1)