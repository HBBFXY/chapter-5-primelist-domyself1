# main.py
# 在此文件中实现 PrimeList 函数（顶层定义，导入时不执行任何 I/O）

def PrimeList(N):
    """
    返回小于 N 的所有质数，以空格分隔（末尾无空格）
    参数:
        N - 应为整数（函数尝试将可转换为整数的值处理）
    返回:
        str - 所有小于 N 的质数组成的字符串，数字间以单个空格分隔；若无质数则返回空字符串 ""
    """
    # 尝试安全地把 N 转为整数；如果不能转为整数则返回空字符串
    try:
        n = int(N)
    except Exception:
        return ""

    # 对小于等于2的 n 返回空字符串（小于2没有质数）
    if n <= 2:
        return ""

    # 使用埃拉托斯特尼筛法
    sieve = [True] * n  # sieve[i] 表示 i 是否可能为质数
    # 明确标记 0 和 1 为非质数（n >= 3 时这些索引存在）
    sieve[0] = False
    sieve[1] = False

    # 只需筛到 sqrt(n)
    import math
    limit = int(math.isqrt(n)) + 1
    for i in range(2, limit):
        if sieve[i]:
            start = i * i
            # 从 i*i 开始，步长为 i，标记合数
            for j in range(start, n, i):
                sieve[j] = False

    # 收集质数并返回单个空格连接的字符串（确保没有首尾空格）
    primes = [str(i) for i in range(2, n) if sieve[i]]
    return " ".join(primes)


# 不要在导入时执行任何测试或打印；只有直接运行脚本时才示例输出
if __name__ == "__main__":
    # 简短示例（不会在被 autograder import 时执行）
    print(PrimeList(10))  # 期望: 2 3 5 7
