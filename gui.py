from Tkinter import *
from degCon import from_dms, from_dd

class Deg_con_gui(object):
    def __init__(self, master):
	self.master = master
	master.title("Degree converter")

	#Title
	self.title_label = Label(master, text = "Degree converter")
	self.title_label.grid(row = 0, columnspan = 2)

	#Text entry
	self.text_frame = Frame(master)
	self.text_frame.grid(row = 1, column = 0)
	self.dms_frame = Frame(self.text_frame)
	self.dms_frame.grid(row = 0, column = 0, columnspan = 2)
	Label(self.dms_frame, text = "D:").grid(row = 0, column = 0, sticky=E)
	self.degree_entry = Entry(self.dms_frame, width = 3)
	self.degree_entry.grid(row = 0, column = 1, sticky=W)
	Label(self.dms_frame, text = "M:").grid(row = 0, column = 2, sticky=E)
	self.minute_entry = Entry(self.dms_frame, width = 3)
	self.minute_entry.grid(row = 0, column = 3, sticky=W)
	Label(self.dms_frame, text = "S:").grid(row = 0, column = 4, sticky=E)
	self.second_entry = Entry(self.dms_frame, width = 7)
	self.second_entry.grid(row = 0, column = 5, sticky=W)

	self.to_dd_button = Button(self.text_frame, text = "To Dec Degrees", command = self.convert_text_to_dd)
	self.to_dd_button.grid(row = 1, column = 0)
	self.to_dms_button = Button(self.text_frame, text = "To DMS", command = self.convert_text_to_dms)
	self.to_dms_button.grid(row = 1, column = 1)

	Label(self.text_frame, text = "Decimal Degrees:").grid(row = 2, column = 0)
	self.dd_entry = Entry(self.text_frame, width = 13)
	self.dd_entry.grid(row = 2, column = 1)

	#File entry
	self.file_frame = Frame(master)
	self.file_frame.grid(row = 1, column = 1)
	# TODO: Not yet implemented

    def convert_text_to_dd(self):
	# TODO: Catch bad conversions and yell at user
	d = float(self.degree_entry.get()) if self.degree_entry.get() else 0
	m = float(self.minute_entry.get()) if self.minute_entry.get() else 0
	s = float(self.second_entry.get()) if self.second_entry.get() else 0
	dd = from_dms(d, m, s)[0]
	self.dd_entry.delete(0, END)
	self.dd_entry.insert(0, str(dd))

    def convert_text_to_dms(self):
	# TODO: Catch bat conversions and yell at user
	dd = float(self.dd_entry.get()) if self.dd_entry.get() else 0
	d,m,s = from_dd(dd)
	self.degree_entry.delete(0, END)
	self.minute_entry.delete(0, END)
	self.second_entry.delete(0, END)
	self.degree_entry.insert(0, str(d))
	self.minute_entry.insert(0, str(m))
	self.second_entry.insert(0, str(s))


if __name__ == '__main__':
    root = Tk()
    Deg_con_gui(root)
    root.mainloop()
