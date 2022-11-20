def calculation(a, b):
    yield a + b
    yield a - b

print(*calculation(3, 5))