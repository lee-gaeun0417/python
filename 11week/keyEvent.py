import tkinter

# 전역변수
key = ""
cx = 400
cy = 300

# 함수 영역
#키보드 입력으로 위치 변경
def main_proc():
    global cx, cy, key
    if key == "Up":
        cy -= 20
    if key == "Down":
        cy += 20
    if key == "Left":
        cx -= 20
    if key == "Right":
        cx += 20
    
    #시간에 따라 캐릭터가 내려감
    cy += 10

    #변경된 위티의 경계 확인
    if cy < 0: cy = 0
    if cy > 600 : cy = 600 - 40
    if cx < 0 : cx = 0
    if cx > 800-40 : cx = 800 -40



#변경 딘 위치에 이미지를 옮김
    canvas.coords("춘식", cx, cy)
    root.after(100, main_proc)

def key_down(e):
    global key
    key = e.keysym

def key_up(e):
    global key
    key = ""  # 키를 뗐을 때 멈추도록

# 메인 영역
root = tkinter.Tk()
root.title("키 이벤트")
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)  

canvas = tkinter.Canvas(width=800, height=600, bg='skyblue')
canvas.pack()

img = tkinter.PhotoImage(file="C:/Users/user/Desktop/python/11week/춘식.png")
canvas.create_image(400, 300, image=img, tag="춘식")

main_proc()
root.mainloop()