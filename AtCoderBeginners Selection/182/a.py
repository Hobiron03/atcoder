def twiblr() -> int:
    A, B = map(int, input().split(" "))
    return 2 * A + 100 - B


if __name__ == "__main__":
    print(twiblr())
