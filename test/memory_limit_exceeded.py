import random

def fn(a):
    fn(a-1), fn

arr = [random.randint(1, 10000) for _ in range(10000)]

arr2 = [arr[:] for _ in range(10000)]

print(arr[arr[1]])