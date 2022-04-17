def Hanoi(n , s_pole, d_pole, i_pole):           
    if n<=1:
        print(f'diske {n} az {s_pole} -----> {d_pole}')
        return
    Hanoi(n-1, s_pole, i_pole, d_pole)
    print(f'diske {n} az {s_pole} -----> {d_pole}')
    Hanoi(n-1, i_pole, d_pole, s_pole)
 
n = 3
Hanoi(n, 'A', 'C', 'B')