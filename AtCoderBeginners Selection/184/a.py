def determinant():
    a, b = map(int, input().split())
    c, d = map(int, input().split())

    result = a*d - b*c
    print(result)


if __name__ == "__main__":
    determinant()
