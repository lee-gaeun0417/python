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
    neko.append([0] * 10)
    check.append([0] * 10)

def load_hisc():
    try:
        file = open("hisc.txt", "r", encoding="utf-8")
        data = file.readline().strip()
        file.close()
        if data.isdigit():
            return int(data)
    except FileNotFoundError:
        return 0
    return 0

def save_hisc():
    file = open("hisc.txt", "w", encoding="utf-8")
    file.writelines(str(hisc))
    file.close()

def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

def mouse_press(e):
    global mouse_c
    mouse_c = 1

def esc_press(e):
    global index, timer, score, tsugi, cursor_x, cursor_y, mouse_c, difficulty, joker_counter, no_input_timer
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
                cvs.create_image(x * 72 + 60, y * 72 + 60, image=img_neko[neko[y][x]], tag="NEKO")

def check_neko():
    for y in range(12):
        for x in range(10):
            check[y][x] = neko[y][x]

    for y in range(1, 11):
        for x in range(10):
            a = check[y][x]
            if a > 0:
                if (check[y-1][x] == a or check[y-1][x] == 7 or a == 7) and \
                   (check[y+1][x] == a or check[y+1][x] == 7 or a == 7):
                    neko[y-1][x] = 7
                    neko[y][x] = 7
                    neko[y+1][x] = 7

    for y in range(12):
        for x in range(1, 9):
            a = check[y][x]
            if a > 0:
                if (check[y][x-1] == a or check[y][x-1] == 7 or a == 7) and \
                   (check[y][x+1] == a or check[y][x+1] == 7 or a == 7):
                    neko[y][x-1] = 7
                    neko[y][x] = 7
                    neko[y][x+1] = 7

    for y in range(1, 11):
        for x in range(1, 9):
            a = check[y][x]
            if a > 0:
                if (check[y-1][x-1] == a or check[y-1][x-1] == 7 or a == 7) and \
                   (check[y+1][x+1] == a or check[y+1][x+1] == 7 or a == 7):
                    neko[y-1][x-1] = 7
                    neko[y][x] = 7
                    neko[y+1][x+1] = 7
                if (check[y+1][x-1] == a or check[y+1][x-1] == 7 or a == 7) and \
                   (check[y-1][x+1] == a or check[y-1][x+1] == 7 or a == 7):
                    neko[y+1][x-1] = 7
                    neko[y][x] = 7
                    neko[y-1][x+1] = 7

    for y in range(11):
        for x in range(9):
            a = check[y][x]
            if a > 0:
                if (check[y][x+1] == a or check[y][x+1] == 7 or a == 7) and \
                   (check[y+1][x] == a or check[y+1][x] == 7 or a == 7) and \
                   (check[y+1][x+1] == a or check[y+1][x+1] == 7 or a == 7):
                    neko[y][x] = 7
                    neko[y][x+1] = 7
                    neko[y+1][x] = 7
                    neko[y+1][x+1] = 7

def sweep_neko():
    num = 0
    for y in range(12):
        for x in range(10):
            if neko[y][x] == 7:
                neko[y][x] = 0
                num += 1
    return num

def drop_neko():
    flg = False
    for y in range(10, -1, -1):
        for x in range(10):
            if neko[y][x] != 0 and neko[y+1][x] == 0:
                neko[y+1][x] = neko[y][x]
                neko[y][x] = 0
                flg = True
    return flg

def over_neko():
    for x in range(10):
        if neko[0][x] > 0:
            return True
    return False

def set_neko():
    for x in range(10):
        neko[0][x] = random.randint(0, difficulty)

def draw_txt(txt, x, y, siz, col, tg):
    fnt = ("Times New Roman", siz, "bold")
    cvs.create_text(x + 2, y + 2, text=txt, fill="black", font=fnt, tag=tg)
    cvs.create_text(x, y, text=txt, fill=col, font=fnt, tag=tg)

def game_main():
    global index, timer, score, hisc, difficulty, tsugi
    global cursor_x, cursor_y, mouse_c, no_input_timer, joker_counter

    if index == 0:
        hisc = load_hisc()
        draw_txt("야옹야옹", 312, 240, 100, "violet", "TITLE")
        cvs.create_rectangle(168, 384, 456, 456, fill="skyblue", width=0, tag="TITLE")
        draw_txt("Easy", 312, 420, 40, "white", "TITLE")
        cvs.create_rectangle(168, 528, 456, 600, fill="lightgreen", width=0, tag="TITLE")
        draw_txt("Normal", 312, 564, 40, "white", "TITLE")
        cvs.create_rectangle(168, 672, 456, 744, fill="orange", width=0, tag="TITLE")
        draw_txt("Hard", 312, 708, 40, "white", "TITLE")
        index = 1
        mouse_c = 0

    elif index == 1:
        difficulty = 0
        if mouse_c == 1:
            if 168 < mouse_x < 456 and 384 < mouse_y < 456:
                difficulty = 4
            if 168 < mouse_x < 456 and 528 < mouse_y < 600:
                difficulty = 5
            if 168 < mouse_x < 456 and 672 < mouse_y < 744:
                difficulty = 6
        if difficulty > 0:
            for y in range(12):
                for x in range(10):
                    neko[y][x] = 0
            mouse_c = 0
            score = 0
            timer = 0
            tsugi = 0
            no_input_timer = 0
            joker_counter = 0
            cursor_x = 0
            cursor_y = 0
            set_neko()
            draw_neko()
            cvs.delete("TITLE")
            index = 2

    elif index in [2, 3, 4, 5]:
        timer += 1

    if index == 2:
        if not drop_neko():
            index = 3
        draw_neko()

    elif index == 3:
        check_neko()
        draw_neko()
        index = 4

    elif index == 4:
        sc = sweep_neko()
        for pos in joker_positions:
            y, x = pos
            if neko[y][x] == 7:
                neko[y][x] = random.randint(1, difficulty)
        joker_positions.clear()
        score += sc * difficulty * 2
        if sc >= 10:
            score += (sc // 10) * 10
        if score > hisc:
            hisc = score
        if sc > 0:
            index = 2
        else:
            if not over_neko():
                if joker_counter > 0 and joker_counter % 5 == 0:
                    tsugi = 7
                else:
                    tsugi = random.randint(1, difficulty)
                index = 5
            else:
                index = 6
                timer = 0
        draw_txt("BREAK " + str(sc), 312, 100, 32, "red", "INFO")
        draw_neko()

    elif index == 5:
        no_input_timer += 1
        if 24 <= mouse_x < 24 + 72 * 10 and 24 <= mouse_y < 24 + 72 * 12:
            cursor_x = int((mouse_x - 24) / 72)
            cursor_y = int((mouse_y - 24) / 72)
            if mouse_c == 1:
                mouse_c = 0
                neko[cursor_y][cursor_x] = tsugi
                if tsugi == 7:
                    joker_positions.append((cursor_y, cursor_x))
                joker_counter += 1
                tsugi = 0
                index = 2
                no_input_timer = 0
        if no_input_timer >= 50 and tsugi > 0:
            for y in range(12):
                for x in range(10):
                    if neko[y][x] == 0:
                        neko[y][x] = tsugi
                        tsugi = 0
                        index = 2
                        no_input_timer = 0
                        break
                if index == 2:
                    break
        cvs.delete("CURSOR")
        cvs.create_image(cursor_x * 72 + 60, cursor_y * 72 + 60, image=cursor, tag="CURSOR")
        draw_neko()
        if tsugi == 7:
            draw_txt("JOKER!", 752, 200, 24, "red", "INFO")

    elif index == 6:
        timer += 1
        if timer == 1:
            draw_txt("GAME OVER", 312, 348, 60, "red", "OVER")
        if timer == 50:
            cvs.delete("OVER")
            save_hisc()
            index = 0

    cvs.delete("INFO")
    draw_txt("SCORE " + str(score), 160, 60, 32, "blue", "INFO")
    draw_txt("HISC " + str(hisc), 450, 60, 32, "yellow", "INFO")
    draw_txt("TIME " + str(timer), 312, 60, 32, "green", "INFO")
    if tsugi > 0:
        cvs.create_image(752, 128, image=img_neko[tsugi], tag="INFO")
    root.after(100, game_main)

root = tkinter.Tk()
root.title("블록 낙하 퍼즐 '야옹야옹'")
root.resizable(False, False)
root.bind("<Motion>", mouse_move)
root.bind("<ButtonPress>", mouse_press)
root.bind("<Escape>", esc_press)
cvs = tkinter.Canvas(root, width=912, height=864)
cvs.pack()

bg = tkinter.PhotoImage(file="neko_bg.png")
cursor = tkinter.PhotoImage(file="neko_cursor.png")
img_neko = [
    None,
    tkinter.PhotoImage(file="neko1.png"),
    tkinter.PhotoImage(file="neko2.png"),
    tkinter.PhotoImage(file="neko3.png"),
    tkinter.PhotoImage(file="neko4.png"),
    tkinter.PhotoImage(file="neko5.png"),
    tkinter.PhotoImage(file="neko6.png"),
    tkinter.PhotoImage(file="neko7.png")
]

cvs.create_image(456, 432, image=bg)
game_main()
root.mainloop()
