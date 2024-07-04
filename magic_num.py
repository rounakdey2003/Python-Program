lim = int(input('''Is the number magic ??\nEnter a number: '''))
d = lim
s = 0
while d > 0:
    x = d % 10
    s += x
    d = d / 10
t = s
r = 0
while t > 0:
    y = t % 10
    r = r * 10 + y
    t = t / 10
if lim == (s * r):
    print("It's a magic number")
else:
    print("It's not a magic number")