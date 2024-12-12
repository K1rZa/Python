import tkinter as tk
from tkinter import *
from tkinter import filedialog
from random import randint

def calculator(event):
	try:
		string = ent_calc.get()
		result = eval(string)
		lbl2_calc["text"] = result
	except ZeroDivisionError:
		lbl2_calc["text"] = "На ноль делить нельзя"
		
def files(count):
	i = 0
	filename = "random_arr"
	while i < count:
		filename_new = filename + str(i)
		arr_list = []
		file = open(filename_new, "w")
		for c in range(10):
			arr_num = randint(1, 100)
			arr_list.append(arr_num)
		for k in range(len(arr_list)):
			file.wtite(str(arr_list[k])+"\n")	
		file.close()
		i += 1
		
def print_sr():
	count = int(ent_files.get())
	files(count)
	filepath = filedialog.askopenfilename()
	if filepath != "":
		file_read = open(filepath, "r")
		data = file_read.read()
		data_list = data.split("\n")
		data_sum = 0
		for g in range(len(data_list)-1):
			data_sum = data_sum + int(data_list[g])
		data_sr = data_sum / (len(data_list)-1)
		lbl2_files["text"] = data_sr
		file_read.close()
		
def classes():
	class All_Name:
		def __init__(self, name):
			self.name = name
		def print_name(name):
			lbl1_classes["text"] = name
			
	class First_name(All_Name):
		def __init__(self, name, group):
			super().__init__(name)
			self.group = group
		def all_name(self):
			All_Name.print_name(self.name)
			lbl2_classes["text"] = self.group
		
	student1 = First_name("Кирилл", "Исдо-33")
	student1.all_name()
		
root = Tk()
root.title("Лаба 6")
root.geometry("600x400")
root["bg"] = "red"

lbl1_calc = Label(root, text="Введите выражение для расчета: ")
ent_calc = Entry(root, width=10)
btn_calc = Button(root, text="=", width=20)
lbl2_calc = Label(root, text="")

lbl1_calc.grid(column=0, row=0)
ent_calc.grid(column=1, row=0)
btn_calc.grid(column=2, row=0, padx=(5, 5), pady=(5, 5))
lbl2_calc.grid(column=3, row=0)

lbl1_calc["bg"] = "red"
lbl2_calc["bg"] = "red"
lbl1_calc["fg"] = "black"
lbl2_calc["fg"] = "black"

btn_calc.bind('<Button-1>', calculator)

lbl1_files = Label(root, text="Введите количество файлов для создания: ")
ent_files = Entry(root, width=10)
btn_files = Button(root, text="Среднее значение: ", width=20, command=print_sr)
lbl2_files = Label(root, text="")

lbl1_files.grid(column=0, row=1)
ent_files.grid(column=1, row=1)
btn_files.grid(column=2, row=1, padx=(5, 5), pady=(5, 5))
lbl2_files.grid(column=3, row=1)

lbl1_files["bg"] = "red"
lbl2_files["bg"] = "red"
lbl1_files["fg"] = "black"
lbl2_files["fg"] = "black"

lbl1_classes = Label(root, text="")
btn_classes = Button(root, text="Показать имя", width=20, command=classes)
lbl2_classes = Label(root, text="")

lbl1_classes.grid(column=0, row=2)
btn_classes.grid(column=2, row=2, padx=(5, 5), pady=(5, 5))
lbl2_classes.grid(column=1, row=2)

lbl1_classes["bg"] = "red"
lbl2_classes["bg"] = "red"
lbl1_classes["fg"] = "black"
lbl2_classes["fg"] = "black"

root.mainloop()