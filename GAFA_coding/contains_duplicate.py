def has_duplicate(array: list) -> bool:

    elements = {}
    for el in array:
        if el in elements:
            elements[el] = True
            return True
        else:
            elements[el] = False

    return False


if __name__ == "__main__":
    print(has_duplicate([1, 2, 3, 4, 5]))
