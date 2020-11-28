def main():
    N, A, B = map(int, input().split())

    # res = 0
    # for n in range(0, N + 1):
    #     digits_num_str = list(str(n))
    #     digits_num_int = [int(i) for i in digits_num_str]

    #     if A <= sum(digits_num_int) <= B:
    #         res += n
    # print(res)

    res = 0
    for n in range(0, N + 1):
        sum_val = find_sum_of_digits(n)
        if A <= sum_val <= B:
            res += n

    print(res)


def find_sum_of_digits(n):
    sum_val = 0
    while(1):
        sum_val += n % 10
        n = n // 10

        if n == 0:
            sum_val += n
            break

    return sum_val


if __name__ == "__main__":
    main()
