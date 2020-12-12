def remove_elements(nums: list, target: int) -> list:
    targetAreaStartIndex = 0
    runnerIndex = 0

    while runnerIndex < len(nums):
        if nums[runnerIndex] != target:
            temp = nums[runnerIndex]
            nums[runnerIndex] = nums[targetAreaStartIndex]
            nums[targetAreaStartIndex] = temp
            targetAreaStartIndex += 1
        runnerIndex += 1

    return targetAreaStartIndex


if __name__ == "__main__":
    print(remove_elements([3, 2, 2, 3, 8], 3))
    # [2,2,8, 3,3]
