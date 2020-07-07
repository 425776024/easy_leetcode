def replaceBlank(str, length):
    s = ''
    for i in range(length):
        if str[i] == ' ':
            str[i] = '%20'
        s += str[i]
    return s

print('<iframe src="//player.bilibili.com/player.html?aid=201217632&bvid=BV1cz411v7ST&cid=208409331&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>')
if __name__ == '__main__':
    str = "Mr John Smith"
    str = list(str)
    a = replaceBlank(str, len(str))
    print(a)
