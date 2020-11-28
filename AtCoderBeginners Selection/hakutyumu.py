def main():
    S = input()
    S = S.replace('eraser', '')
    S = S.replace('erase', '')
    S = S.replace('dreamer', '')
    S = S.replace('dream', '')

    if S:
        print('No')
    else:
        print('Yes')


if __name__ == "__main__":
    main()
