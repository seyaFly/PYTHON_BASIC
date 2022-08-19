# coding=utf-8

# 斐波拉契数列
grantparent, parents, babies = (1, 1, 1)
while babies < 50:
    print('This generation has {0} babies'.format(grantparent))
    parents, babies = (babies, parents + babies)
