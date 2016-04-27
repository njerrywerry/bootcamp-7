# a = [12, 45, 3, 5, 7, 13]
#
# # for x in a:
# #     print x
# #     pass
#
# # print in reverse
# i = len(a)
# while i > 0:
#     print a[i - 1]
#     i -= 1
#
# for x in range(len(a) - 1, -1, -1):
#     print a[x]
#
b = [(2, 4), (5, 10), (6, 20), (50, 50)]
# print output as e.g x: 2, y: 4

for items in b:
    print "x: {}, y: {}".format(items[0], items[1])


arr = [(10, 20, 30), (3, 4), (20, 30, 40)]
# print output as each value with each tuple
