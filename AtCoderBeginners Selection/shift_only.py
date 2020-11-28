def main():
    input()
    A = list(map(int, input().split()))
    count = 0
    while all([num % 2 == 0 for num in A]):
        A = [i / 2 for i in A]
        count += 1
    print(count)


if __name__ == "__main__":
    main()
