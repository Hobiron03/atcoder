import sys


def main():
    N, Y = map(int, input().split())

    total = 0
    for x in range(0, N+1):
        for y in range(0, N-x+1):
            z = N - x - y
            total = 10000*x + 5000*y + 1000*z
            if total == Y:
                print(x, y, z)
                sys.exit()
    print(-1, -1, -1)


if __name__ == "__main__":
    main()
