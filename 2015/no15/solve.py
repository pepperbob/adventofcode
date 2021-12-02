import numpy as np

Sprinkles = np.array([5, -1, 0, 0, 5])
PeanutButter = np.array([-1, 3, 0, 0, 1])
Frosting = np.array([0, -1, 4, 0, 6])
Sugar = np.array([-1, 0, 0, 2, 8])

curr = 0
curr_500 = 0
for a in range(101):
    for b in range(101-a):
        rest = 100-a-b
        ca = np.arange(rest+1)
        da = rest - ca
        for c, d in zip(ca,da):
            cookie = a*Sprinkles + b*PeanutButter + c*Frosting + d*Sugar
            
            nocals = cookie[:-1]
            nocals[nocals<0]=0
            rs = np.prod(nocals)
            if rs > curr:
                curr = rs

            if cookie[-1] == 500 and rs > curr_500:
                curr_500 = rs

print(curr)
print(curr_500)