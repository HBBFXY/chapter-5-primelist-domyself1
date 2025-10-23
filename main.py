def PrimeList(N):
    """
    返回小于 N 的所有质数，以空格分隔    
    参数:    N - 正整数    
    返回:    str - 包含所有小于 N 的质数的字符串，空格分隔
    """
    # 处理边界情况：小于等于2的数没有小于它的质数
    if N <= 2:
        return ""
    
    primes = []
    
    # 检查每个数是否为质数
    for num in range(2, N):
        is_prime = True
        
        # 检查num是否为质数
        if num == 2:
            is_prime = True
        elif num % 2 == 0:
            is_prime = False
        else:
            # 只需要检查到sqrt(num)
            for i in range(3, int(num ** 0.5) + 1, 2):
                if num % i == 0:
                    is_prime = False
                    break
        
        if is_prime:
            primes.append(str(num))
    
    # 用空格连接所有质数
    return " ".join(primes)
