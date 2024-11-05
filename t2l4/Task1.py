#S = √(р (р — а)(р — b)(p — c)) 
a,b,c = map(float, input("Enter 3 edges: ").split())
per = a + b + c
p = per/2
s = (p * (p - a) * (p - b) * (p - c))**0.5
print("perim = ", per, "square = ", s)

