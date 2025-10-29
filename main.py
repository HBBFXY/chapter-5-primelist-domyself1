def PrimeList(N):
    """
    返回小于 N 的所有质数，以空格分隔
    参数: N - 整数
    返回: 小于N的所有质数，以空格分隔(末尾无空格)
    """
    # 处理边界情况：N <= 2 时没有质数
    if N <= 2:
        return ""
    
    # 使用埃拉托斯特尼筛法
    sieve = [True] * N
    sieve[0] = False  # 0不是质数
    if N > 1:
        sieve[1] = False  # 1不是质数
    
    # 筛法核心算法
    for i in range(2, int(N**0.5) + 1):
        if sieve[i]:
            # 从i*i开始标记非质数
            for j in range(i*i, N, i):
                sieve[j] = False
    
    # 收集所有质数
    primes = []
    for i in range(2, N):
        if sieve[i]:
            primes.append(str(i))
    
    # 以空格连接，确保末尾无空格
    return " ".join(primes)
print(PrimeList(10)) 
