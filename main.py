# 在此文件中实现 PrimeList 函数

def PrimeList(N):
    """
    返回小于 N 的所有质数，以空格分隔    
    参数:    N - 正整数    
    返回:    str - 包含所有小于 N 的质数的字符串，空格分隔
    """
    # 负数、0、1、2的情况
    if N <= 2:
        return ""

    primes = []
    # 使用埃拉托斯特尼筛法（高效）
    sieve = [True] * N
    sieve[0:2] = [False, False]  # 0和1不是质数

    for i in range(2, int(N ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, N, i):
                sieve[j] = False

    for i in range(2, N):
        if sieve[i]:
            primes.append(str(i))

    return " ".join(primes)
