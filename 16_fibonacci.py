# for loops
def fibo(n):
    last = 0
    prev = 1
    curr = 0
    print(last)
    print(prev)
    for i in range(2, n):
        curr = last + prev
        last = prev
        prev = curr
        print(curr)


fibo(7)
print("\n")
lst = [21, 314, 43, 41, 34, 14]
for it in lst:
    print(it)

tpl = (21, 131, 23, 14, 124, 12, 4)
for i in tpl:
    print(i)
