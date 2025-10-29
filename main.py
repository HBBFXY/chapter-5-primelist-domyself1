def PrimeList(n):
    """
    返回小于 N 的所有质数，以空格分隔    
    参数:    N - 正整数    
    返回:    str - 包含所有小于 N 的质数的字符串，空格分隔
    """
    # 负数、0、1、2的情况
    if n <= 2:
        return ""

    primes = []
    # 使用埃拉托斯特尼筛法（高效）
    sieve = [True] * n
    sieve[0:2] = [False, False]  # 0和1不是质数

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n, i):
                sieve[j] = False

    for i in range(2, n):
        if sieve[i]:
            primes.append(str(i))

    return " ".join(primes)

# 获取用户输入
N = int(input("请输入一个正整数N: "))
result = PrimeList(N)
print(f"小于{N}的所有质数为: {result}")
