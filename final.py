import r3ad
import op3n

list1 = r3ad.read()


def fun1(c):
    sum1 = 0
    for x in range(c, 90, 22):
        sum1 = sum1 + list1[x]
    print((c+1), ' : ', sum1)
    op3n.write2(str(c+1) + ' : ' + str(sum1) + '\n')


for x in range(0, 22):
    fun1(x)
