# pre: hello
# post: olleh


def reverse_string(string: str) -> str:
    str_array = list(string)
    start = 0
    end = len(string) - 1
    # 二分探索で両端から検索
    while start < end:
        temp = str_array[start]
        str_array[start] = str_array[end]
        str_array[end] = temp

        start += 1
        end -= 1

    return "".join(str_array)


if __name__ == "__main__":
    print(reverse_string("Hello,world, my name is jun"))
