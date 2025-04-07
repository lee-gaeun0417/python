import tkinter

root = tkinter.Tk()
root.title("캔버스 만들기")

# 캔버스 생성
canvas = tkinter.Canvas(root, width=400, height=600)
canvas.pack()

# 캔버스 이미지 생성
bgimg = tkinter.PhotoImage(file="miko.png")  
canvas.create_image(400, 300, image=bgimg)  

# 좌표 출력기
def mouseMove(event):
    x = event.x
    y = event.y
    labelMouse["text"] = str(x) + "," + str(y)

root.bind("<Motion>", mouseMove) 

labelMouse = tkinter.Label(root, text=",", font=("맑은 고딕", 10))  
labelMouse.pack()

root.mainloop()
