def countAndSay(n):
    if n == 0:
        return ''
    res = '3'
    while n != 0:
        n -= 1
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
        print(res)
    return res

print('<iframe src="//player.bilibili.com/player.html?aid=328784792&bvid=BV1WA411e7Cy&cid=209612236&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>')
s = countAndSay(6)
