def Sort(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]


print('<iframe src="//player.bilibili.com/player.html?aid=243715980&bvid=BV11v411B7Ey&cid=207954392&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>')
if __name__ == '__main__':
    arr = [1, 4, 3, 7, 8, 10, 9, 2, 11]
    Sort(arr)
    print(arr)
