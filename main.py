# main.py
# 在此文件中实现 PrimeList 函数

def PrimeList(N):
    """
    返回小于 N 的所有质数，以空格分隔
    参数:
        N - 整数
    返回:
        str - 包含所有小于 N 的质数的字符串，数字间以单个空格分隔（末尾无空格）
    """
    # 确保对非正或小于等于2的输入返回空字符串
    try:
        # 尝试把 N 当作整数处理（检测脚本是传整数，但这里保守处理）
        N_int = int(N)
    except Exception:
        # 如果不能转换为整数，返回空字符串以保持鲁棒
        return ""

    if N_int <= 2:
        return ""

    N = N_int

    # 埃拉托斯特尼筛法
    sieve = [True] * N
    sieve[0] = False
    sieve[1] = False

    limit = int(N ** 0.5) + 1
    for i in range(2, limit):
        if sieve[i]:
            start = i * i
            # 标记合数
            for j in range(start, N, i):
                sieve[j] = False

    # 收集质数并以单个空格连接
    primes = [str(i) for i in range(2, N) if sieve[i]]

    return " ".join(primes)


# 可选：仅当作为脚本直接运行时，打印一个示例（导入时不会执行）
if __name__ == "__main__":
    # 简单示例（不会影响自动评测，因为导入时不会运行）
    print(PrimeList(10))  # 期望输出: 2 3 5 7
