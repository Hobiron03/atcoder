def return_majority_element(nums: list) -> list:
    nums_dic = {}
    max_count_num = 0
    max_count = 0
    for num in nums:
        if num in nums_dic:
            nums_dic[num] += 1
        else:
            nums_dic[num] = 1

    for k, v in nums_dic.items():
        if v > max_count:
            max_count = v
            max_count_num = k

    return max_count_num


if __name__ == "__main__":
    res = return_majority_element([3, 5, 7, 2, 3, 3, 3, 8, 12, 5, 43, 1])

    print(res)
