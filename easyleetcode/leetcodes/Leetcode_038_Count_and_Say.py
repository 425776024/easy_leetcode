def countAndSay(n):
    if n == 0:
        return ''
    res = '2'
    while n != 0:
        n -= 1
        print(res)
        i = 0
        count = 1
        cur = ''
        # 拼接res的读数
        while i < len(res):
            count = 1
            # 有下一个，且下一个字母相等
            while i + 1 < len(res) and res[i] == res[i + 1]:
                count += 1
                i += 1
            # 数量+本身
            cur += str(count) + res[i]
            # 到下一个数字位
            i += 1
        res = cur
    return res


s = countAndSay(6)
