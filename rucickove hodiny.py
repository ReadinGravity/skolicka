ret=input('zadaj mi retazec (hh:mm):')
a,b,=ret.split(':')
a=int(a)
b=int(b)
m_angle=6*b
h_angle=30*a+b/60*30
print(abs(m_angle-h_angle))


