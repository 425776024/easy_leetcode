def Sort(arr):
    for i in range(len(arr)):
        min_i = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]
    return arr

print('<iframe src="//player.bilibili.com/player.html?aid=371135586&bvid=BV1wZ4y1p7Fe&cid=207954024&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>')
if __name__ == '__main__':
    arr = Sort([3, 5, 1, 2, 6, 7, 9, 11,22])
    print(arr)

    