def is_right_triangle(a,b,c):
    if a+b>=c and b+c>=a and c+a>=b:
        print("Right")
    else:
        print("Not Right")
# Reading Three Sides
side_a = float(input('Enter length of side a: '))
side_b = float(input('Enter length of side b: '))
side_c = float(input('Enter length of side c: '))
# Function call & making decision
is_right_triangle(side_a, side_b, side_c)
