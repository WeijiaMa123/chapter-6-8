import turtle




path=[(160, 20), (-43, 10), (270, 8), (-43, 12)]

for (angle,dist) in path:
    print("angle",angle)
    print("distance",dist)






def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
        
