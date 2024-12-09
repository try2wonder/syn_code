mike = int(input("Mike money: "))
ivan = int(input("ivan money: "))
min_inv = int(input("Min investment: "))

if mike > min_inv and ivan > min_inv:
    print("2")
elif mike > min_inv:
    print("Mike")
elif ivan > min_inv:
    print("ivan")
elif (mike + ivan) > min_inv:
    print("1")
else:
    print("0")
