import math

a, b, h, m = map(int, input().split())
h_theta = 2*math.pi * (60*h + m) / (60*12)
m_theta = 2*math.pi * m / 60
delta = h_theta-m_theta if h_theta>m_theta else m_theta-h_theta
l2 = a**2 + b**2 - 2*a*b*math.cos(delta)
print(math.sqrt(l2))