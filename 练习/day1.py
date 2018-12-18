# 1、
# l1 = sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])
# print(l1)

# 2、
# nums = [1, 6, 6, 3, 6, 2, 10, 2, 100]
#
#
# def remove_nums(num):
#     # print(num)
#     # if num != 6:
#     return num
#
#
# l2 = sorted(map(remove_nums, nums), reverse=True)
# print(l2)

# 3、
nums1 = [1, 3, 3, 5, 5, 8, 10, 10, 100, 100]
# (1)
l3 = []
for i in nums1:
    if i not in l3:
        l3.append(i)
print(l3)
# (2)
l4 = sorted(list(set(nums1)))
print(l4)

# 4、
# nums2 = [1,1,1,2,2,3]
# for i in nums2:
#     if

