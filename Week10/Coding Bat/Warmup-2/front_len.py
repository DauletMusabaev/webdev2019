def front_times(str, n):
    l = 3
    if l > len(str):
        l = len(str)
    front = str[:3]

    a = ""
    for i in range(n):
        a = a + front
    return a