a = int(input())
b = int(input())

nums2 = "The Array is: "

for i in range (a,b+1):
    if i % 2 == 0:
        nums2 += str(i) 
        nums2 += " "
print(nums2)