from tkinter import *

top = Tk()

top.title("my windows")
top.geometry("400x200")


# first_l = BooleanVar()
# # first_l = False
# def command_w():
#     print(first_l.get())

# r1 = Radiobutton(
#     top,
#     text="general",
#     variable=first_l,
#     value = True,
#     command = command_w).pack()

# r2 = Radiobutton(
#     top,
#     text="anime",
#     variable=first_l,
#     value = False,
#     command = command_w).pack()

# r3 = Radiobutton(
#     top,
#     text="people",
#     variable=first_l,
#     value = True,
#     command = command_w).pack()

group = Frame(top, padx=30, pady=30)
group.pack(padx=30, pady=0)
a = Label(group,bg = 'yellow',text='EMPTY')
a.pack()
def show_choice():
    a.config(text=' is '+str(ani.get()))
    # if ani.get() == 1:
    #     print('a')
    # else:
    #     print('b')

gener = IntVar()
ani = IntVar()
peo = IntVar()
c1 = Checkbutton(group,text = "general", variable = gener,onvalue = 1,offvalue = 0,indicatoron = False,command = show_choice)
c1.pack()
# c1.pack()
c2 = Checkbutton(group,text = "anime", variable = ani,onvalue = 1,offvalue = 0,command = show_choice)
# c2.pack()
c2.pack()
c3 = Checkbutton(group,text = "people", variable = peo,onvalue = 1,offvalue = 0,indicatoron = False,command = show_choice)
# c3.place(x=110,y=0,width=55)
c3.pack()

# butter1 = Button(top,text ="hello world",activebackground = 'yellow',command = command_w,image = "people").pack()

# butter1.pack()

top.mainloop()