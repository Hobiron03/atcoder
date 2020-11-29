def check_two_sum(target: int, array: list) -> bool:
    # targe - array[i] = x
    # このxが配列の中に存在するか
    hash = {}
    for el in array:
        if target-el in hash:
            return True

        hash[el] = el
    return False


if __name__ == "__main__":
    print(check_two_sum(4, [1, 4, 3, 2]))
