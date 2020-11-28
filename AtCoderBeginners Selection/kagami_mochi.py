def main():
    N = int(input())
    num_list = [int(input()) for _ in range(N)]

    # sorted_num_list = sorted(num_list, reverse=True)
    # res = 0
    # current_diameter = 0
    # for num in sorted_num_list:
    #     if current_diameter == num:
    #         continue
    #     else:
    #         res += 1
    #         current_diameter = num

    # print(res)

    res_dic = {}
    for num in num_list:
        if num in res_dic:
            res_dic[num] += 1
        else:
            res_dic[num] = 1

    print(len(res_dic))


if __name__ == "__main__":
    main()
