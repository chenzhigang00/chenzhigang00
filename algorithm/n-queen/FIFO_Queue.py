# n-皇后问题，FIFO先进先出分支限界法
from queue import Queue
n = int(input())

def place(k, x):
    for j in range(1, k):
        # 与之前所放皇后不在同一斜线，且不在同一列
        if abs(j - k) == abs(x[j] - x[k]) or x[j] == x[k]:
            return False
    return True

### ———————————————— FIFO队列 ———————————————— ###
q = Queue()
k = 1
ans = []
cur_choose = [0]

while True:
    if k > n:    # 叶子节点
        flag = True
        ans.append(cur_choose[1:])

        if q.empty():
           break
        else:
           cur_choose = q.get()

    else:     # 非叶子节点
        # 加入节点
        if k == 1:    # 对称剪枝
            times = (n + 1) // 2
            for i in range(1, times + 1):
                tmp = cur_choose[:]
                tmp.append(i)
                if place(k, tmp):  # 可行性剪枝
                    q.put(tmp)
        else:
            for i in range(1, n + 1):
                tmp = cur_choose[:]
                tmp.append(i)
                if place(k, tmp):    # 可行性剪枝
                    q.put(tmp)

        # 取节点
        if q.empty():
            flag = False
            break
        else:
            cur_choose = q.get()
            k = len(cur_choose)

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

if flag:
    print(len(ans))
    print(ans)
    for k in range(len(ans)):
        for j in range(n):
            a = ans[k][j]
            for i in range(a - 1):
                print(".",end='')
            print("Q",end='')
            for i in range(n - a):
                print(".",end='')
            print()
        print()
else:
    print("无解")
