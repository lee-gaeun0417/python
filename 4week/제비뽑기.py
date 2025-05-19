import tkinter
import random

root = tkinter.Tk()
root.title("캔버스 만들기")

# 캔버스 생성
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()

# 좌표 출력기
def mouseMove(event):
    x = event.x
    y = event.y
    labelMouse["text"] = str(x) + "," + str(y)

root.bind("<Motion>", mouseMove) 

# 랜덤 출력
def click_btn():
    label["text"] = random.choice(["대길","중길","소길","흉"])
    text.insert(tkinter.END,label["text"]+"\n")

labelMouse = tkinter.Label(root, text=",", font=("맑은 고딕", 10))  
labelMouse.pack()

# 캔버스 이미지 생성
bgimg = tkinter.PhotoImage(file="C:/Users/user/Desktop/python/4week/miko.png")  
canvas.create_image(400, 300, image=bgimg)  

canvas.create_rectangle(350,390,620,520, fill='darkgray', outline ='red', width='3')

label = tkinter.Label(root, text="??", font=("맑은 고딕", 120))
label.place(x=380, y=60)

button = tkinter.Button(root, text= "제비 뽑기", font= ("맑은 고딕", 36), command= click_btn )
button.place(x=360, y= 400)

text = tkinter.Text()
text.pack()


root.mainloop()
