import timeit

print timeit.timeit(stmt="10**7 in l", setup="l = range(10**6)", number=10)
print timeit.timeit(stmt="10**7 in l", setup="l = range(10**6)", number=100)
print timeit.timeit(stmt="10**7 in l", setup="l = range(10**6)", number=1000)
print timeit.timeit(stmt="10**7 in s", setup="s = set(range(10**6))", number=1000)
print timeit.timeit(stmt="10**7 in s", setup="s = set(range(10**6))", number=10000)
print timeit.timeit(stmt="10**7 in s", setup="s = set(range(10**6))", number=100000)

