import time

y0 = 100
t = 0
a = -0.5
v0 = 0

while True:

    v = v0 + a*t
    y = y0 + v0*t + a*t**2/2

    if y<=0:
        t = 0
        v0 = -v
        y0 = 0

    print(f'y={y}, v={v}, t={t}')
    time.sleep(0.1)
    t += 1