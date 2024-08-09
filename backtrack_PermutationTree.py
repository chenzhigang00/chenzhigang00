# n-皇后问题，排列树做法
n = int(input())
x = [0] * (n + 1)    # 每行皇后的摆放位置（存储列:1 ~ n）

tmp = [0] * (n + 1)  # 位置
for i in range(1, n + 1):
    tmp[i] = i        # tmp[1:] = [1, 2, 3, ..., n], 构造排列选择
ans = []

def place(k):
    global x
    for j in range(1, k):
        # 与之前所放皇后不在同一斜线
        if abs(j - k) == abs(x[j] - x[k]):
            return False
    return True

def backtrack(k):
    global ans, x, a
    if k > n:       # 叶子结点处，得到可行解
        ans.append(x[1:])        # 深拷贝
    else:
        if k == 1:              # 对称剪枝，可直接推算另一半的最优解情况
            times = (n + 1) // 2
            for i in range(1, times + 1):
                x[k] = tmp[i]
                if place(k):  # 可行性剪枝，检查该处是否能放皇后
                    tmp[k], tmp[i] = tmp[i], tmp[k]  # 构造全排列
                    backtrack(k + 1)
                    tmp[k], tmp[i] = tmp[i], tmp[k]
        else:
            for i in range(k, n + 1):
                x[k] = tmp[i]
                if place(k):     # 可行性剪枝，检查该处是否能放皇后
                    tmp[k], tmp[i] = tmp[i], tmp[k]    # 构造全排列
                    backtrack(k + 1)
                    tmp[k], tmp[i] = tmp[i], tmp[k]

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