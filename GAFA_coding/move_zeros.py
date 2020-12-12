def move_zeros(nums: list) -> list:
    runnerIndex = 0
    zeroStartIndex = 0

    while runnerIndex < len(nums):
        if nums[runnerIndex] != 0:
            temp = nums[runnerIndex]
            nums[runnerIndex] = nums[zeroStartIndex]
            nums[zeroStartIndex] = temp
            zeroStartIndex += 1

        runnerIndex += 1

    return nums


if __name__ == "__main__":
    print(move_zeros([1, 0, 38, 12, 0, 111, 0]))
