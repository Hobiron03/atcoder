def main():
    A_500_num = int(input())
    B_100_num = int(input())
    C_50_num = int(input())
    X_sum = int(input())

    combi_count = 0
    total = 0
    for a in range(0, A_500_num + 1):
        for b in range(0, B_100_num + 1):
            for c in range(0, C_50_num + 1):
                total = 500 * a + 100 * b + 50 * c
                if total == X_sum:
                    combi_count += 1

    print(combi_count)


if __name__ == "__main__":
    main()
