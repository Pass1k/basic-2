a = [-1, 2, -3, 4, -5]

b = list(map(abs, a))
c = [abs(i)for i in a]
print(b)
print(c)


def f(x):
    return x**2


g = list(map(f, a))
print(g)


r = ['hello', 'hi', 'good morning']
c = [i[::-1] for i in r]

print(list(map(len, r)))
print(list(map(str.upper, r)))
print(c)


s = list(map(int, input().split()))
print(s)