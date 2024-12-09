m = int(input())
n = int(input())
mfish = 0 #fishermen in boat total mass
seatcount = 0
boats = 1
for i in range (n):
    fish1 = int(input())
    if fish1 <= (m - mfish) and seatcount <2:
        mfish += fish1
        seatcount += 1
        print(f"Welcome aboard!, now we have {2-seatcount} seats left and {m - mfish} kilos left")
    else:
        print("Sorry, we need another boat")
        boats += 1
        seatcount = 0
        mfish = 0
        mfish += fish1
        seatcount += 1
        print(f"The new boat has {2-seatcount} seats left and {m - mfish} kilos left")

print(boats)
        
# Boat = m kg and/or 2 ppl




