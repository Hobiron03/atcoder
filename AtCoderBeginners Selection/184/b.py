def quizzes():
    _, X = map(int, input().split())
    S = input()

    for i in S:
        if i == 'o':
            X += 1
        else:
            X = X-1 if X > 0 else 0

    print(X)


if __name__ == "__main__":
    quizzes()
