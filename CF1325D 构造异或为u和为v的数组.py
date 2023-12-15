u, v = map(int, input().split())
if u > v or u & 1 != v & 1:
    print(-1)
elif u == v:
    if u != 0:
        print(1)
    print(u)
else:
    d = v - u
    if d & 1:
        print(-1)
    else:
        x = d >> 1
        if (u + x) ^ x == u:
            print(2)
            print(u + x, x)
        else:
            print(3)
            print(u, x, x)
