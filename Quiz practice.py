x = "abc" + "3"

y = x + str(float(4))

print(y)

#...................................................
a = b = 8

c, d = 8, 8

print(id(a),id(b),id(c),id(d))

#...................................................
firstVar = 4

sndVar = 3 + firstVar

#...................................................

print(2j * (3 + 4j))

#...................................................


m = int(input('Enter an integer: '))

if (m < 1000):

    p = 2000 / m

print('p=' , p)

#...................................................
listt=[1,2,4,5,6,6,8,9]
print(*listt)
print(*range(1,20,2))

#...................................................

p = -5
q = 0
while p < 4:
    p += 1
    if p == 0: continue
    q += 12 / p
print(int(q))

#...................................................
