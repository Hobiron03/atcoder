def arrege_even_odd(nums: list) -> list:
    oddStartIndex = 0
    runnnerIndex = 0

    while runnnerIndex < len(nums):
        if isEven(nums[runnnerIndex]):
            # swap
            temp = nums[runnnerIndex]
            nums[runnnerIndex] = nums[oddStartIndex]
            nums[oddStartIndex] = temp
            oddStartIndex += 1
        runnnerIndex += 1
    return nums


def isEven(num: int) -> bool:
    if num % 2 == 0:
        print("True")
        return True
    return False


if __name__ == "__main__":
    print(arrege_even_odd([0, 1, 3, 4, 2, 4, 5, 1, 6, 9, 8]))
    # [0, 1, 3, 4, 2, 4, 5, 1, 6, 9, 8] -> [0,4,2,4,6,8,1,3,5,1,9]
