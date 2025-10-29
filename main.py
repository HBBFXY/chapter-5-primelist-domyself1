def PrimeList(N):
    """
    返回小于 N 的所有质数，以空格分隔
    参数: N - 整数
    返回: 小于N的所有质数，以空格分隔(末尾无空格)
    """
    # 处理边界情况：N <= 2 时没有质数
    if N <= 2:
        return ""
    
    # 处理负数输入
    if N < 0:
        N = -N
    
    # 使用埃拉托斯特尼筛法
    sieve = [True] * N
    sieve[0] = sieve[1] = False  # 0和1不是质数
    
    # 筛法核心算法
    for i in range(2, int(N**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, N, i):
                sieve[j] = False
    
    # 收集所有质数
    primes = []
    for i in range(2, N):
        if sieve[i]:
            primes.append(str(i))
    
    # 以空格连接，确保末尾无空格
    return " ".join(primes)

# 添加输入输出部分以满足交互需求
if __name__ == "__main__":
    try:
        n = int(input("请输入一个整数N: "))
        result = PrimeList(n)
        if result:
            print(f"小于{n}的所有质数为: {result}")
        else:
            print(f"小于{n}的质数不存在")
    except ValueError:
        print("输入错误，请输入一个整数")
