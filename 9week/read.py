import tkinter

root = tkinter.Tk()

file = open("C:/Users/user/Desktop/python/9week/test.txt", "r", encoding="utf-8")

strfile = file.readline()
root.geometry(strfile[:-1])

strfile = file.readline()
root.title(strfile[:-1])



file.close()  

root.mainloop()


'''
index= 1
for strlist in filelist:
    print(str(index)+":"+strlist,end="")
    index


while True:
    str = file.readline()
    print(str,end='')
    if(str==""):
        break


'''