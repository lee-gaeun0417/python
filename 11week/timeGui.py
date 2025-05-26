import tkinter

# 전역변수
tmr = 0

def countUp():
    global tmr
    tmr += 1
    label["text"] = tmr
    root.after(100, countUp)

root = tkinter.Tk()
root.title("타이머")
root.geometry("300x200")

label = tkinter.Label(text="0", font=("궁서체", 80))
label.pack()

root.after(1000, countUp)
root.mainloop()
