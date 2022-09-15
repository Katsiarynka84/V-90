a, b = input(), input()
try:
    print(int(a) + int(b))
except ValueError:
    print(a + b)
