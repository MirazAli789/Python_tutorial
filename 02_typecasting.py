a = "123"
print(a, type(a), sep="~")
b = 123
print(b, type(b), sep="~")
print(a + 12)  # exception
print(int(a) + 12)  # no exception ~~~~~~ typecasting
