import tkinter
root = tkinter.Tk()
root.title("캔버스 만들기")

# 캔버스 생성
canvas = tkinter.Canvas(root, width= 400, height=600)
canvas.pack()

# 캔버스 이미지 생성
bgimg = tkinter.PhotoImage(fille = 'miko.png')
canvas.create_image(400,300,Image= bgimg)


root.mainloop()