def write1():
    fw = open("miziz.txt", "a")
    for i in range(100, 111):
        new = str(i)
        fw.write('(' + new + ',  ) \n')
    fw.close()


def write2(text):
    f = open("new3.txt", "a+")
    f.write(text)
    f.close()

