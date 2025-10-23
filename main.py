def PrimeList(N):
    """
    返回小于 N 的所有质数，以空格分隔    
    参数:    N - 正整数    
    返回:    str - 包含所有小于 N 的质数的字符串，空格分隔
    """
    # 处理边界情况
    if N <= 2:
        return ""
    
    # 处理负数和无效输入
    if N < 0:
        return ""
    
    # 使用埃拉托斯特尼筛法
    if N <= 2:
        return ""
    
    # 创建标记数组，初始都设为True
    is_prime = [True] * N
    is_prime[0] = False  # 0不是质数
    if N > 1:
        is_prime[1] = False  # 1不是质数
    
    # 筛法核心
    for i in range(2, int(N**0.5) + 1):
        if is_prime[i]:
            # 将i的倍数标记为非质数
            for j in range(i*i, N, i):
                is_prime[j] = False
    
    # 收集所有质数
    primes = []
    for i in range(2, N):
        if is_prime[i]:
            primes.append(str(i))
    
    # 用空格连接并返回
    return " ".join(primes)
