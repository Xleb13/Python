# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk

def btn_1():
    a = txt1.get()
    i = 1
    n = int(a)
    s = " "
    while i ** 2 < n:
        s += str(i**2)
        i += 1
        s = s + " "
    vihd1.configure(text = s)

def btn_2():
    a = txt2.get()
    n = int(a)
    i = 2
    while n % i != 0:
        i += 1
    vihd2.configure(text = i)

def btn_3():
    a = txt3.get()
    n = int(a)
    i = 2
    e = 1
    while i <= n:
        i *= 2
        e += 1
    result = "Показатель степени : " + str(e-1) + " " + "Степень : " + str(i // 2)
    vihd3.configure(text = result)

def btn_4():
    x = int(txt4.get())
    y = int(txt4_1.get())
    n = 1
    while x < y:
        x *= 1.1
        n += 1
    n = "Потребуется " + str(n) + " дней"
    vihd4.configure(text = n)


k = 0
def btn_5():
    global k
    a = txt5.get()
    print(a)
    if(a != "0"):
        k += 1
    else:
        vihd5.configure(text = k)
    txt5.delete(0, END)



x = 0
y = 0
def btn_6():
    global y
    a = txt6.get()
    print(a)
    global x
    if a != "0":
        y += 1
        x += int(a)
    else:
        vihd6.configure(text = x / y)
    txt6.delete(0, END)

b = 0
a = 10000000
def btn_7():
    n = txt7.get()
    print(n)
    global b
    global a
    if(int(n) > a):
        b+=1
    a = int(n)
    if(n == "0"):
        vihd7.configure(text = b)
    txt7.delete(0, END)



window = Tk()
window.title("Практическая работа №6")
window.wm_attributes('-alpha',0.95)
window.geometry('700x280')


tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)
tab6 = ttk.Frame(tab_control)
tab7 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Первая')
tab_control.add(tab2, text='Вторая')
tab_control.add(tab3, text='Третья')
tab_control.add(tab4, text='Четвертая')
tab_control.add(tab5, text='Пятая')
tab_control.add(tab6, text='Шестая')
tab_control.add(tab7, text='Седьмая')

#вкладка_1
lbl1 = Label(tab1, text = "Введите число")
lbl1.grid(column=0, row = 0)
txt1 = Entry(tab1, width = 10)
txt1.grid(column=1, row = 0)
btn1 = Button(tab1, text = "Ввод", command = btn_1)
btn1.grid(column=2, row = 0)
vhd1 = Label(tab1, text = " Результат: ")
vhd1.grid(column = 3, row = 0)
vihd1 = Label(tab1, text ="")
vihd1.grid(column=4, row = 0)

#вкладка_2
lbl2 = Label(tab2, text = "Введите число")
lbl2.grid(column=0, row = 1)
txt2 = Entry(tab2, width = 10)
txt2.grid(column=1, row = 1)
btn2 = Button(tab2, text = "Ввод",command = btn_2)
btn2.grid(column=2, row = 1)
vhd2 = Label(tab2, text = "Результат : ")
vhd2.grid(column = 3, row = 1)
vihd2 = Label(tab2, text = "")
vihd2.grid(column=4, row = 1)

#вкладка_3
lbl3 = Label(tab3, text = "Введите число")
lbl3.grid(column=0, row = 2)
txt3 = Entry(tab3, width = 10)
txt3.grid(column=1, row = 2)
btn3 = Button(tab3, text = "Ввод", command = btn_3)
btn3.grid(column=2, row = 2)
vhd3 = Label(tab3, text = "Результат : ")
vhd3.grid(column = 3, row = 2)
vihd3 = Label(tab3, text = "")
vihd3.grid(column=4, row = 2)

#вкладка_4
lbl4 = Label(tab4, text = "Введите начальный и конечный результат")
lbl4.grid(column=0, row = 3)
txt4 = Entry(tab4, width = 10)
txt4.grid(column=1, row = 3)
txt4_1 = Entry(tab4, width = 10)
txt4_1.grid(column=2, row = 3)
btn4 = Button(tab4, text = "Ввод", command=btn_4)
btn4.grid(column=3, row = 3)
vhd4 = Label(tab4, text = "Результат : ")
vhd4.grid(column = 4, row = 3)
vihd4 = Label(tab4, text = "")
vihd4.grid(column=5, row = 3)

#вкладка_5
lbl5 = Label(tab5, text = "Число 0 выведет результат")
lbl5.grid(column=0, row = 4)
txt5 = Entry(tab5, width = 10)
txt5.grid(column=1, row = 4)
btn5 = Button(tab5, text = "Ввод", command=btn_5)
btn5.grid(column=2, row = 4)
vhd5 = Label(tab5, text = "Результат: ")
vhd5.grid(column = 3, row = 4)
vihd5 = Label(tab5, text = "")
vihd5.grid(column=4, row = 4)

#вкладка_6
lbl6 = Label(tab6, text = "Введите последовательность : ")
lbl6.grid(column=0, row = 5)
txt6 = Entry(tab6, width = 10)
txt6.grid(column=1, row = 5)
btn6 = Button(tab6, text = "Ввод", command=btn_6)
btn6.grid(column=2, row = 5)
vhd6 = Label(tab6, text = "Результат: ")
vhd6.grid(column = 3, row = 5)
vihd6 = Label(tab6, text = "")
vihd6.grid(column=4, row = 5)

#вкладка_7
lbl7 = Label(tab7, text = "Введите последовательность")
lbl7.grid(column=0, row = 6)
txt7 = Entry(tab7, width = 10)
txt7.grid(column=1, row = 6)
btn7 = Button(tab7, text = "Ввод", command=btn_7)
btn7.grid(column=2, row = 6)
vhd7 = Label(tab7, text = "Элементов : ")
vhd7.grid(column = 3, row = 6)
vihd7 = Label(tab7, text = "")
vihd7.grid(column=4, row = 6)




tab_control.pack(expand=1, fill='both')

window.mainloop()