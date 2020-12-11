def calc_max_gcd_num(nums: list) -> int:
    max_gcd = 0
    max_gcd_num = 0
    for i in range(2, max(nums)+1):
        # step2:iのgcpを求める
        gcd = 0
        for num in nums:
            if num % i == 0:
                gcd += 1

        # step3: if gcdがmax_gcdより多ければswap
        if gcd > max_gcd:
            max_gcd = gcd
            max_gcd_num = i

    return max_gcd_num


if __name__ == "__main__":
    _ = int(input())
    nums = list(map(int, input().split()))
    print(calc_max_gcd_num(nums))
