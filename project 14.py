def bmm(a , b):
    if(b == 0):
        return a
    return bmm(b , a % b)




a = int(input('enter a number: '))

b = int(input('enter a number: '))

print('bmm = ' , bmm(a , b))

input()