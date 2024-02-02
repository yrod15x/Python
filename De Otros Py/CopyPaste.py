nums = [1,2,3,1,2]
c = 0
for i in range(0, 4):
    if i == -1:
        continue
    else:
        for j in range(i, 4):
            if nums[i] == nums[j + 1]:
                nums[j + 1] = -1
for i in nums:
    if i != -1:
        c += 1
print(c)
