# n-皇后问题，子集树做法
n = int(input())
x = [0] * (n + 1)    # 每行皇后的摆放位置（存储列:1 ~ n）
ans = []

def place(k):
    global x
    for j in range(1, k):
        # 与之前所放皇后不在同一列也不在同一斜线
        if x[k] == x[j] or abs(j - k) == abs(x[j] - x[k]):
            return False
    return True

def backtrack(k):
    global ans, x, a
    if k > n:       # 叶子结点处，得到可行解
        ans.append(x[1:])        # 深拷贝
    else:
        if k == 1:   # 对称剪枝
            times = (n + 1) // 2
            for i in range(1, times + 1):
                x[k] = i  # 放置皇后
                if place(k):  # 可行性约束剪枝
                    backtrack(k + 1)
        else:
            for i in range(1, n + 1):
                x[k] = i   # 放置皇后
                if place(k):    # 可行性约束剪枝
                    backtrack(k + 1)

backtrack(1)
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



print(len(ans))
print(ans)