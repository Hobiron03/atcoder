def move_zeros(nums: list) -> list:
    runnerIndex = 0
    nonZeroIndex = 0

    while runnerIndex < len(nums):
        if nums[runnerIndex] != 0:
            temp = nums[runnerIndex]
            nums[runnerIndex] = nums[nonZeroIndex]
            nums[nonZeroIndex] = temp
            nonZeroIndex += 1

        runnerIndex += 1

    return nums


def swap(a, b):
    pass


if __name__ == "__main__":
    print(move_zeros([1, 0, 38, 12, 0, 111, 0]))
