# 测试题1
# count = 0
# a = 1
# b = 1
# for i in range(20):
#     a, b = b, a + b
#     count += (a+b/a)
# print(count)


# 测试题2
# a = input("请输入一个五位数：").strip()
# if a[0] == a[4]:
#     if a[1] == a[3]:
#         print("它是一个回文数")
# else:
#     print("他不是一个回文数")

# 测试题3
# import random
#
# def random_num():
#     ran_list = []
#     for i in range(20):
#         ran = random.randint(0,100)
#         ran_list.append(ran)
#     for j in ran_list:
#         if j >= 80:
#             print("成绩为:",j,"等级为:",'A')
#         elif 80>j>=60:
#             print("成绩为:",j,"等级为:",'B')
#         else:
#             print("成绩为:",j,"等级为:",'C')
# random_num()


# 测试题4

# class Parent(object):
#     x = 1
# class Child1(Parent):
#     pass
# class Child2(Parent):
#     pass
# print(Parent.x, Child1.x, Child2.x)
# Child1.x = 2
# print(Parent.x, Child1.x, Child2.x)
# Parent.x = 3
# print (Parent .x, Child1.x, Child2.x)
# 1、
#  1 2 1
# 2、
# Parent.x = 3


# x = 40 + 200 + 2.5*25
# print(x)
#
# y = x*1.2394
# print(y)
#
# print(400 - y)


# nums = [2,3,5,7,9]
# news_nums = []
# for i in range(len(nums) - 1):
#     for j in range(len(nums) - 1 - i):
#         if nums[i] + nums[j] == 7:
#             news_nums.insert(nums[i],nums[j])
# print(news_nums)

# class Solution:
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         print(len(nums))
#         for i in range(len(nums) - 1):
#             print(len(nums)-1-i)
#
#             for j in range(i+1,len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return i,j
#         return []
#
# a = Solution()
# print(a.twoSum([3,2,4],6))


# l1 = [2,4,3]
# l2 = [5,6,4]
# l1.reverse()

# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         l1.reverse()
#         l2.reverse()


# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         tmpnode = ListNode(0)  # 第一个节点需要舍弃
#         res = tmpnode  # 返回值
#         add = 0  # 进位
#         while l1 or l2:
#             tmpsum = add
#             if l1:
#                 tmpsum += l1.val
#                 l1 = l1.next
#
#             if l2:
#                 tmpsum += l2.val
#                 l2 = l2.next
#
#             add = tmpsum // 10
#             tmpnode.next = ListNode(tmpsum % 10)
#             tmpnode = tmpnode.next
#         if add != 0:  # 处理最后的进位
#             tmpnode.next = ListNode(add)
#         return res.next
#
#
# a = Solution()
# print(a.addTwoNumbers(l1,l2))

#
# a = 10
# b = bin(a)
# int
# print(int(b,2))

# input("asdasda")



# l1 = ['sean','yang','1','2','python','5']
# l2 = []
# for i in l1:
#     if i.isdigit():
#         l2.append(i)
#     else:
#         print("xxx")
# print(l2)

# l3 = [1,'ddd','sss',4,'eee']
#
# for i in l3:
#     if type(i) == int:
#         print(i)

# print('\n'.join([''.join([('LoveDaLin'[(x-y)%8]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))


