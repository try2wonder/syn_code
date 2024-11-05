number = int(input())
description = "Число"

if number < 0:
    description += " отрицательное"
elif number > 0:
    description += " положительное"
else:
    description += " нулевое"

if number % 2 == 0:
    description += " чётное"
else:
    description += " нечётное"

print(description)

