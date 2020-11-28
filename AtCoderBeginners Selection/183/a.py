def ReLU(x: int):
    if x >= 0:
        return x
    else:
        return 0


if __name__ == "__main__":
    x = int(input())
    result = ReLU(x)
    print(result)
