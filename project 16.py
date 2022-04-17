def number_len(n):
    c = 0
    while(n != 0):
        n//=10
        c+= 1
    return c

def power_digits(n , p):
    s = 0
    while(n != 0):
        r = n % 10
        s += r ** p
        n//=10
    return s

for i in range(1 , 10000 + 1):
    l = number_len(i)
    s = power_digits(i , l)
    if(s == i):
        print(s , end = ',')


input()


