def replace_spy(spy):
    spy[2] = spy[2] + 1
    return spy
print(replace_spy([0 , 0 , 7]))

a = 3
def inc(n):
    n = n + 1
    return n
print(inc(a))