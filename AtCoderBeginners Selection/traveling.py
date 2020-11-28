import sys


def main():
    N = int(input())
    num_list = []
    for i in range(N):
        num_list.append(list(map(int, input().split())))

    prev_t = 0
    prev_x = 0
    prev_y = 0
    for nums in num_list:
        t = nums[0]
        x = nums[1]
        y = nums[2]
        diff_t = abs(t - prev_t)
        dist = abs(x - prev_x) + abs(y - prev_y)

        if dist > diff_t:
            print('No')
            sys.exit()

        if diff_t % 2 != dist % 2:
            print('No')
            sys.exit()

        prev_t = t
        prev_x = x
        prev_y = y

    print('Yes')


if __name__ == "__main__":
    main()
