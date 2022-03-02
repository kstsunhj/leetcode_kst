def countBits(n):
    res = []
    for r in range(n + 1):
        res_bin = bin(r)
        num = 0
        for i in res_bin:
            if i == '1':
                num+=1
        res.append(num)
    return res