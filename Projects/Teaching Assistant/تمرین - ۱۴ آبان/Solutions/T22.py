for t in range(0,1000):
    for i in range(1, 8):
        s = ""
        for j in range(1, i+1):
            s += str(j)
        for j in range(i-1, 0, -1):
            s += str(j)
        print (s)
