import time

n = 1_000_000
big_list = list(range(n))
big_set = set(big_list)

target = n - 1

t0 = time.perf_counter()
target in big_list
t1 = time.perf_counter()
target in big_set
t2 = time.perf_counter()

print(f"list scan  : {(t1 - t0) * 1000:9.4f} ms")
print(f"set lookup : {(t2 - t1) * 1000:9.4f} ms")
print(f"ratio      : {(t1 - t0) / (t2 - t1):,.0f}x")
