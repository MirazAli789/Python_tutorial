# while loops are also used for continuously doing something
i = 0
while i <= 10:
    print(i)
    i += 1

r = 9
while r >= 0:
    print(r)

    r -= 1

# while True:
#     num = int(input("enter a number \n"))
#     if num == 0:
#         break
# print("program finished executing")

i = 0
while i <= 20:
    print(i)
    i += 1
    if i == 14:
        continue
    

print("program ends execution")

# r = 10
# while r <= 30:
#     if r == 14:
#         r += 1
#         continue

#     print(r)
#     r += 1

i = 10
n = int(input("enter a range"))
while i <= n:
    if i == 13:

        i += 1
        continue
    elif i == 30:
        break
    print(i)
    i += 1
