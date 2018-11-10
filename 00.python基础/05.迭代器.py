from collections import Iterator

a = (x for x in range(5))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

print(isinstance(a, Iterator))
