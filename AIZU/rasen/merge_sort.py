counter = 0


def main():
    ary_length = int(input())
    ary = list(map(int, input().split()))

    global counter
    sorted_list = merge_sort(ary)

    print(sorted_list)
    print(counter)


def merge_sort(ary):
    if len(ary) <= 1:
        return ary

    mid = len(ary) // 2
    left = ary[:mid]
    right = ary[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    l_i, r_i = 0, 0
    global counter
    while l_i < len(left) and r_i < len(right):
        counter += 1
        if left[l_i] <= right[r_i]:
            merged.append(left[l_i])
            l_i += 1
        else:
            merged.append(right[r_i])
            r_i += 1

    if l_i < len(left):
        merged.extend(left[l_i:])

    if r_i < len(right):
        merged.extend(right[r_i:])

    return merged


if __name__ == "__main__":
    main()
