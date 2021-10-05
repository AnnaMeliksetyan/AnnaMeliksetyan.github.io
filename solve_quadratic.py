def solve_quadratic(a,b,c): 
    from math import sqrt
    discriminant = ( b * b ) - 4*a*c
    
    if discriminant > 0:
        return (-b-sqrt (discriminant))/(2*a),(-b+sqrt(discriminant))/(2*a) 
    elif discriminant == 0:
        return (-b+sqrt(discriminant))/(2*a)
    else:
        return None
