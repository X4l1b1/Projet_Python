
from Tkinter import *
import ttk

#Game dimensions
WDTH = 700
HGTH = 700
NB_COL = 7
NB_ROW = 6

#Frames dimensions
WDTH_F1 = WDTH
HGTH_F1 = HGTH - (HGTH / (NB_ROW + 1))
WDTH_F2 = WDTH
HGTH_F2 = HGTH - NB_ROW*(HGTH / (NB_ROW + 1))

#Columns dimensions
WDTH_COL = WDTH_F1 / NB_COL
HGTH_COL = HGTH_F1


root = Tk()

#Content root Frame
content = ttk.Frame(root)
content.pack(side=LEFT, expand = 1)


#Globale Frames
frame1 = ttk.Frame(content, width = WDTH_F1, height = HGTH_F1)

frame2 = ttk.Frame(content, width = WDTH_F2, height = HGTH_F2)

frame1.pack(expand = 1)
frame2.pack(expand = 1)


#Canvas Columns for frame1
columns = []
for i in range(NB_COL):
	columns.append(Canvas(frame1, width = WDTH_COL, height = HGTH_COL, background = "blue")) #TODO: COLOR CONSTANT
	columns[i].grid(column = i, row = 0)

#Draw the circles
offset = WDTH_COL / 20
HGTH_CASE = HGTH_COL / NB_ROW

columns_grid = [ [ columns[j].create_oval(offset, i*HGTH_CASE + offset,
				 WDTH_COL - offset, (i + 1)*HGTH_CASE - offset, fill = 'white') for j in range(NB_COL) ]
			 for i in range(NB_ROW)]




columns[0].itemconfig(columns_grid[0][0], fill='red')


root.mainloop()