import tkinter
import random
import os
import tkinter.messagebox

index = 0
timer = 0
score = 0
hisc = 0
difficulty = 0
tsugi = 0
joker_counter = 0
no_input_timer = 0
joker_positions = []

cursor_x = 0
cursor_y = 0
mouse_x = 0
mouse_y = 0
mouse_c = 0

neko = []
check = []
for i in range(12):
    neko.append([0]*10)
    check.append([0]*10)

def load_hisc():
    try:
        with open("hisc.txt", "r", encoding="utf-8") as file:
            data = file.readline().strip()
            if data.isdigit():
                return int(data)
    except FileNotFoundError:
        return 0
    return 0

def save_hisc():
    with open("hisc.txt", "w", encoding="utf-8") as file:
        file.write(str(hisc))

def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

def mouse_press(e):
    global mouse_c
    mouse_c = 1

def esc_press(e):
    global index, timer, score, tsugi, cursor_x, cursor_y, mouse_c
    global difficulty, joker_counter, no_input_timer
    if tkinter.messagebox.askyesno("경고", "게임을 종료하시겠습니까?"):
        index = 0
        timer = 0
        score = 0
        tsugi = 0
        joker_counter = 0
        no_input_timer = 0
        cursor_x = 0
        cursor_y = 0
        mouse_c = 0
        difficulty = 0
        for y in range(12):
            for x in range(10):
                neko[y][x] = 0
        cvs.delete("NEKO")
        cvs.delete("CURSOR")
        cvs.delete("INFO")
        cvs.delete("OVER")
        cvs.delete("TITLE")

def draw_neko():
    cvs.delete("NEKO")
    for y in range(12):
        for x in range(10):
            if neko[y][x] > 0:
                cvs.create_image(x*72+24, y*72+24, image=img_neko[neko[y][x]], tag="NEKO")

def check_neko():
    for y in range(12):
        for x in range(10):
            check[y][x] = neko[y][x]

    for y in range(1,11):
        for x in range(10):
            a = check[y][x]
            if a > 0:
                if (check[y-1][x] in (a,7) or a==7) and (check[y+1][x] in (a,7) or a==7):
                    neko[y-1][x] = neko[y][x] = neko[y+1][x] = 7

    for y in range(12):
        for x in range(1,9):
            a = check[y][x]
            if a > 0:
                if (check[y][x-1] in (a,7) or a==7) and (check[y][x+1] in (a,7) or a==7):
                    neko[y][x-1] = neko[y][x] = neko[y][x+1] = 7

    for y in range(1,11):
        for x in range(1,9):
            a = check[y][x]
            if a > 0:
                if (check[y-1][x-1] in (a,7) or a==7) and (check[y+1][x+1] in (a,7) or a==7):
                    neko[y-1][x-1] = neko[y][x] = neko[y+1][x+1] = 7
                if (check[y+1][x-1] in (a,7) or a==7) and (check[y-1][x+1] in (a,7) or a==7):
                    neko[y+1][x-1] = neko[y][x] = neko[y-1][x+1] = 7

    for y in range(11):
        for x in range(9):
            a = check[y][x]
            if a > 0:
                if (check[y][x+1] in (a,7) or a==7) and (check[y+1][x] in (a,7) or a==7) and (check[y+1][x+1] in (a,7) or a==7):
                    neko[y][x] = neko[y][x+1] = neko[y+1][x] = neko[y+1][x+1] = 7

def sweep_neko():
    num = 0
    for y in range(12):
        for x in range(10):
            if neko[y][x]==7:
                neko[y][x]=0
                num+=1
    return num

def drop_neko():
    flg=False
    for y in range(10,-1,-1):
        for x in range(10):
            if neko[y][x]!=0 and neko[y+1][x]==0:
                neko[y+1][x]=neko[y][x]
                neko[y][x]=0
                flg=True
    return flg

def over_neko():
    return any(neko[0][x]>0 for x in range(10))

def set_neko():
    global tsugi
    tsugi = random.randint(1, difficulty)

def draw_txt(txt,x,y,siz,col,tg):
    fnt=("Times New Roman",siz,"bold")
    cvs.create_text(x+2,y+2,text=txt,fill="black",font=fnt,tag=tg)
    cvs.create_text(x,y,text=txt,fill=col,font=fnt,tag=tg)

def game_main():
    global index,timer,score,hisc,difficulty,tsugi
    global cursor_x,cursor_y,mouse_c,no_input_timer,joker_counter

    if index==0:
        hisc=load_hisc()
        draw_txt("야옹야옹",312,240,100,"violet","TITLE")
        cvs.create_rectangle(168,384,456,456,fill="skyblue",width=0,tag="TITLE")
        draw_txt("Easy",312,420,40,"white","TITLE")
        cvs.create_rectangle(168,528,456,600,fill="lightgreen",width=0,tag="TITLE")
        draw_txt("Normal",312,564,40,"white","TITLE")
        cvs.create_rectangle(168,672,456,744,fill="orange",width=0,tag="TITLE")
        draw_txt("Hard",312,708,40,"white","TITLE")
        index=1
        mouse_c=0

    elif index==1:
        difficulty=0
        if mouse_c==1:
            if 168<mouse_x<456 and 384<mouse_y<456: difficulty=4
            if 168<mouse_x<456 and 528<mouse_y<600: difficulty=5
            if 168<mouse_x<456 and 672<mouse_y<744: difficulty=6
        if difficulty>0:
            for y in range(12):
                for x in range(10):
                    neko[y][x]=0
            mouse_c=0
            score=0
            timer=0
            tsugi=0
            no_input_timer=0
            joker_counter=0
            cursor_x=0
            cursor_y=0
            set_neko()
            draw_neko()
            cvs.delete("TITLE")
            index=5

    elif index in [2,3,4,5]:
        timer+=1

    if index==2:
        if not drop_neko():
            index=3
        draw_neko()

    elif index==3:
        check_neko()
        draw_neko()
        index=4

    elif index==4:
        sc=sweep_neko()
        score+=sc*difficulty*2
        if sc>=10:
            score+=(sc//10)*10
        if score>hisc:
            hisc=score
        if sc>0:
            index=2
        else:
            if not over_neko():
                set_neko()
                index=5
            else:
                index=6
                timer=0
        draw_txt("BREAK "+str(sc),312,100,32,"red","INFO")
        draw_neko()

    elif index==5:
        no_input_timer+=1
        if 24<=mouse_x<24+72*10 and 24<=mouse_y<24+72*12:
            cursor_x=int((mouse_x-24)/72)
            cursor_y=int((mouse_y-24)/72)
            if mouse_c==1:
                mouse_c=0
                if neko[cursor_y][cursor_x]==0:
                    neko[cursor_y][cursor_x]=tsugi
                    tsugi=0
                    index=2
                    no_input_timer=0
        if no_input_timer>=50 and tsugi>0:
            for y in range(12):
                for x in range(10):
                    if neko[y][x]==0:
                        neko[y][x]=tsugi
                        tsugi=0
                        index=2
                        no_input_timer=0
                        break
                if index==2:
                    break
        cvs.delete("CURSOR")
        cvs.create_image(cursor_x*72+24,cursor_y*72+24,image=cursor,tag="CURSOR")
        draw_neko()

    elif index==6:
        timer+=1
        if timer==1:
            draw_txt("GAME OVER",312,348,60,"red","OVER")
        if timer==50:
            cvs.delete("OVER")
            save_hisc()
            index=0

    cvs.delete("INFO")
    draw_txt("SCORE "+str(score),160,60,32,"blue","INFO")
    draw_txt("HISC "+str(hisc),450,60,32,"yellow","INFO")
    draw_txt("TIME "+str(timer),312,60,32,"green","INFO")
    if tsugi>0:
        cvs.create_image(752,128,image=img_neko[tsugi],tag="INFO")
    root.after(100,game_main)

root=tkinter.Tk()
root.title("블록 낙하 퍼즐 '야옹야옹'")
root.resizable(False,False)
root.bind("<Motion>",mouse_move)
root.bind("<ButtonPress>",mouse_press)
root.bind("<Escape>",esc_press)

# 경로 수정하세요
bg=tkinter.PhotoImage(file=r"C:\Users\USER\Desktop\python\[가상현실프로그래밍] 기말 프로젝트 기본 코드\neko_bg.png")
cursor=tkinter.PhotoImage(file=r"C:\Users\USER\Desktop\python\[가상현실프로그래밍] 기말 프로젝트 기본 코드\neko_cursor.png")
img_neko=[
    None,
    tkinter.PhotoImage(file=r"C:\Users\USER\Desktop\python\[가상현실프로그래밍] 기말 프로젝트 기본 코드\neko1.png"),
    tkinter.PhotoImage(file=r"C:\Users\USER\Desktop\python\[가상현실프로그래밍] 기말 프로젝트 기본 코드\neko2.png"),
    tkinter.PhotoImage(file=r"C:\Users\USER\Desktop\python\[가상현실프로그래밍] 기말 프로젝트 기본 코드\neko3.png"),
    tkinter.PhotoImage(file=r"C:\Users\USER\Desktop\python\[가상현실프로그래밍] 기말 프로젝트 기본 코드\neko4.png"),
    tkinter.PhotoImage(file=r"C:\Users\USER\Desktop\python\[가상현실프로그래밍] 기말 프로젝트 기본 코드\neko5.png"),
    tkinter.PhotoImage(file=r"C:\Users\USER\Desktop\python\[가상현실프로그래밍] 기말 프로젝트 기본 코드\neko6.png"),
    tkinter.PhotoImage(file=r"C:\Users\USER\Desktop\python\[가상현실프로그래밍] 기말 프로젝트 기본 코드\neko7.png")
]

canvas_width=bg.width()
canvas_height=bg.height()
cvs=tkinter.Canvas(root,width=canvas_width,height=canvas_height)
cvs.pack()
cvs.create_image(0,0,image=bg,anchor="nw")

game_main()
root.mainloop()

