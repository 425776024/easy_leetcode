# 插入排序，o(n^2)

def Sort(arr):
    n = len(arr)
    for i in range(1, n):  # 第一个数直接进入数组
        # i代表了当前排序数组的长度，arr[i]代表新的需要插入的数，从最后一个开始比，
		# 比前面的小就要一直往前对换，直到比前面的大
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break

print('<iframe src="//player.bilibili.com/player.html?aid=583640666&bvid=BV1uz4y1X7mx&cid=207954618&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>')
if __name__ == '__main__':
    arr = [1,3, 4, 7, 8, 10, 2, 9, 11]
    Sort(arr)
    print(arr)
