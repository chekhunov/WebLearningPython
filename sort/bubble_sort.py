class Bubble:
    nums = [2, 34, 51, 25, 6, 7, 12, 3, 6, 3, 8, 9, 12, 3, 6, 3, 212, 1]
    print(nums)
    count = len(nums)

    for i in range(count - 1):
        for j in range(count - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    print(nums)
