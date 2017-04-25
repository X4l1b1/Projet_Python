
from Tkinter import *
import ttk

root = Tk()


def make_case(case0, case1, case2, case3, case4, case5):
	case0.create_oval(5, 5, 95, 95, fill = 'white')
	case1.create_oval(5, 5, 95, 95, fill = 'white')
	case2.create_oval(5, 5, 95, 95, fill = 'white')
	case3.create_oval(5, 5, 95, 95, fill = 'white')
	case4.create_oval(5, 5, 95, 95, fill = 'white')
	case5.create_oval(5, 5, 95, 95, fill = 'white')



content = ttk.Frame(root)
canvas0 = Canvas(content, width=100, height=600, background='yellow')
canvas1 = Canvas(content, width=100, height=600, background='orange')
canvas2 = Canvas(content, width=100, height=600, background='red')
canvas3 = Canvas(content, width=100, height=600, background='green')
canvas4 = Canvas(content, width=100, height=600, background='blue')
canvas5 = Canvas(content, width=100, height=600, background='green')
canvas6 = Canvas(content, width=100, height=600, background='blue')

case0 = Canvas(canvas0, width = 100, height = 100, background = 'blue')
case1 = Canvas(canvas0, width = 100, height = 100, background = 'blue')
case2 = Canvas(canvas0, width = 100, height = 100, background = 'blue')
case3 = Canvas(canvas0, width = 100, height = 100, background = 'blue')
case4 = Canvas(canvas0, width = 100, height = 100, background = 'blue')
case5 = Canvas(canvas0, width = 100, height = 100, background = 'blue')

case10 = Canvas(canvas1, width = 100, height = 100, background = 'blue')
case11 = Canvas(canvas1, width = 100, height = 100, background = 'blue')
case12 = Canvas(canvas1, width = 100, height = 100, background = 'blue')
case13 = Canvas(canvas1, width = 100, height = 100, background = 'blue')
case14 = Canvas(canvas1, width = 100, height = 100, background = 'blue')
case15 = Canvas(canvas1, width = 100, height = 100, background = 'blue')


case20 = Canvas(canvas2, width = 100, height = 100, background = 'blue')
case21 = Canvas(canvas2, width = 100, height = 100, background = 'blue')
case22 = Canvas(canvas2, width = 100, height = 100, background = 'blue')
case23 = Canvas(canvas2, width = 100, height = 100, background = 'blue')
case24 = Canvas(canvas2, width = 100, height = 100, background = 'blue')
case25 = Canvas(canvas2, width = 100, height = 100, background = 'blue')


case30 = Canvas(canvas3, width = 100, height = 100, background = 'blue')
case31 = Canvas(canvas3, width = 100, height = 100, background = 'blue')
case32 = Canvas(canvas3, width = 100, height = 100, background = 'blue')
case33 = Canvas(canvas3, width = 100, height = 100, background = 'blue')
case34 = Canvas(canvas3, width = 100, height = 100, background = 'blue')
case35 = Canvas(canvas3, width = 100, height = 100, background = 'blue')




make_case(case0, case1, case2, case3, case4, case5)
make_case(case10, case11, case12, case13, case14, case15)
make_case(case20, case21, case22, case23, case24, case25)
make_case(case30, case31, case32, case33, case34, case35)







content.grid(column=0, row=0,)
canvas0.grid(column=0, row=0, columnspan=1)
canvas1.grid(column=1, row=0, columnspan=1)
canvas2.grid(column=2, row=0, columnspan=1)
canvas3.grid(column=3, row=0, columnspan=1)
canvas4.grid(column=4, row=0, columnspan=1)
canvas5.grid(column=5, row=0, columnspan=1)
canvas6.grid(column=6, row=0, columnspan=1)

case0.grid(column = 0, row = 0)
case1.grid(column = 0, row = 1)
case2.grid(column = 0, row = 2)
case3.grid(column = 0, row = 3)
case4.grid(column = 0, row = 4)
case5.grid(column = 0, row = 5)

case10.grid(column = 0, row = 0)
case11.grid(column = 0, row = 1)
case12.grid(column = 0, row = 2)
case13.grid(column = 0, row = 3)
case14.grid(column = 0, row = 4)
case15.grid(column = 0, row = 5)

case20.grid(column = 0, row = 0)
case21.grid(column = 0, row = 1)
case22.grid(column = 0, row = 2)
case23.grid(column = 0, row = 3)
case24.grid(column = 0, row = 4)
case25.grid(column = 0, row = 5)

case30.grid(column = 0, row = 0)
case31.grid(column = 0, row = 1)
case32.grid(column = 0, row = 2)
case33.grid(column = 0, row = 3)
case34.grid(column = 0, row = 4)
case35.grid(column = 0, row = 5)


root.mainloop()