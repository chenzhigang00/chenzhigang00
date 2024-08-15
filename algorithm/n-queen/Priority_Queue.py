# n-皇后问题_优先队列分支限界法
import heapq

n = int(input())
def place(k, x):
    for j in range(1, k):
        # 与之前所放皇后不在同一斜线，且不在同一列
        if abs(j - k) == abs(x[j] - x[k]) or x[j] == x[k]:
            return False
    return True

class node:
    def __init__(self, choose, depth):
        self.choose = choose
        self.depth = depth

    # 重载"<"运算符，按优先级排序，优先级定义为当前深度
    def __lt__(self, other):
        return self.depth < other.depth

### ———————————————————— 优先队列 —————————————————— ###
h = []   # 大顶堆，深度越深优先级越大，越先扩展
cur_choose = [0]
k = 1
ans = []

while True:
    if k > n:    # 叶子节点
        ans.append(cur_choose[1:])

        if h:
            tmpnode = heapq.heappop(h)
            cur_choose = tmpnode.choose
            k = -tmpnode.depth
        else:    # 优先队列为空
            break

    else:       # 非叶子节点
        # 加入节点
        if k == 1:      # 对称剪枝
            times = (n + 1) // 2
            for i in range(1, times + 1):
                tmp = cur_choose[:]
                tmp.append(i)
                if place(k, tmp):  # 可行性剪枝
                    tmpnode = node(tmp, -(k + 1))  # 大顶堆
                    heapq.heappush(h, tmpnode)

        else:
            for i in range(1, n + 1):
                tmp = cur_choose[:]
                tmp.append(i)
                if place(k, tmp):
                    tmpnode = node(tmp, -(k + 1))    # 大顶堆
                    heapq.heappush(h, tmpnode)

        # 取节点
        if h:
            tmpnode = heapq.heappop(h)
            cur_choose = tmpnode.choose
            k = -tmpnode.depth
        else:   # 队列空
            break

if n % 2 == 0:
    tmp = ans[:]     # 副本，隔绝更新ans带来的影响
    for plan in tmp:
        new_plan = [n + 1 - queen for queen in plan]
        ans.append(new_plan)
else:
    tmp = ans[:]  # 副本，隔绝更新ans带来的影响
    for plan in tmp:
        if plan[0] != (n + 1) // 2:
            new_plan = [n + 1 - queen for queen in plan]
            ans.append(new_plan)

# 输出结果
if ans:
    for item1 in ans:
        for item2 in item1:
            print(item2, end=' ')
        print()
    print()
    for k in range(len(ans)):
        for j in range(n):
            a = ans[k][j]
            for i in range(a - 1):
                print(".", end='')
            print("Q", end='')
            for i in range(n - a):
                print(".", end='')
            print()
        print()
else:
    print("无解")




