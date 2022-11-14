
#write a while loop to print the squares of the numbers: 1, 3, 6, 10, 15 and 21

nums = [1, 3, 6, 10, 15, 21]
i = 0

while i < len(nums):
    square = nums[i] * nums[i]
    print(square)
    i += 1

