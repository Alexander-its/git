print("Привет!")
a = int(input("число: "))
k = 0
for i in range(1, a + 1):
    if a % i == 0:
        k += 1
if k == 2:
    print("простое")
else:
    print("непростое")
    
