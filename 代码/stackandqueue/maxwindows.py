
def getMaxWindow(arr,w):
    if len(arr) == 0 or w < 1 or len(arr) < w:
        return None
    deque = []
    res = []
    for i in range(len(arr)):
        while deque and arr[deque[-1]] <= arr[i]:
            deque.pop()
        deque.append(i)
        #下标过期
        if deque[0] <= i-w:
            deque.pop(0)
        # 窗口形成
        if i-w+1 >= 0:
            res.append(arr[deque[0]])
    return res
