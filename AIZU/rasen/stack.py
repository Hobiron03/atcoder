def main():
    r_p_formula = list(input().split())

    stack = []
    res = 0
    for element in r_p_formula:
        try:
            num = int(element)
            stack.append(num)

        except ValueError:
            last_num = stack.pop()
            sec_last_num = stack.pop()
            stack.append(calc(sec_last_num, last_num, element))

    print(stack.pop())


def calc(num1, num2, ope):
    if ope == "+":
        return num1 + num2
    elif ope == "-":
        return num1 - num2
    elif ope == "*":
        return num1 * num2
    else:
        return 0


if __name__ == '__main__':
    main()
