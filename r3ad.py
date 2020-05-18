import op3n


def read():
    f = open('new2.txt', 'r')
    test = f.read()
    f.close()
    #print(test)
    num2 = list(map(int, test.split()))
    return num2

# test2 = test.replace(" ", "")
# test3 = test2.replace("(", "")
# test4 = test3.replace(")", "")
# op3n.write2(test4)
# test5 = test4.replace("\n", "")
# print(help(test5.split()))
# num2 = list(map(list, test5.split()))
# num2=map(list, test4.split(")"))
# test5=test4.replace(",","")
# num=list(test5)
# new = test5.split()
# d = dict(x.split(",") for x in test3.split(")"))

# for k, v in d.items():
#     print(k, v)
#print(num2[0])
