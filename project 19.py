x = float(input('enter degree: '))
x *= (3.141519 / 180)
sinus = 0
s = 1
for i in range(1 , 40 , 2):
    f = 1
    for j in range(1 , i + 1):
        f*=j
    sinus += s * (x**i) / f
    s*=-1

print('sin=',sinus)
input()