import tkinter

class TKLabels:
	root: tkinter.Tk = None

	def __init__(self, root: tkinter.Tk, click):
		self.root = root
		self.click = click
		self.render()
    
	def render(self):
		self.title_label = tkinter.Label(self.root, text='Решение систем линейных уравнений', font=('Arial', 14, 'bold'))
		self.title_label.pack(side=tkinter.LEFT, anchor=tkinter.N, pady=10)

		self.matrix_entry = tkinter.Frame(self.root)
		self.matrix_entry.place(relx=0.1, rely=0.3, anchor=tkinter.CENTER)

		self.enter_matrix_label = tkinter.Label(self.matrix_entry, text='Матрица')
		self.enter_matrix_label.grid(row=0, column=0, columnspan=2)

		self.matrix_1_entry = tkinter.Entry(self.matrix_entry, width=4)
		self.matrix_1_entry.grid(row=1, column=0)
		self.matrix_2_entry = tkinter.Entry(self.matrix_entry, width=4)
		self.matrix_2_entry.grid(row=1, column=1)
		self.matrix_3_entry = tkinter.Entry(self.matrix_entry, width=4)
		self.matrix_3_entry.grid(row=1, column=2)
		self.matrix_4_entry = tkinter.Entry(self.matrix_entry, width=4)
		self.matrix_4_entry.grid(row=2, column=0)
		self.matrix_5_entry = tkinter.Entry(self.matrix_entry, width=4)
		self.matrix_5_entry.grid(row=2, column=1)
		self.matrix_6_entry = tkinter.Entry(self.matrix_entry, width=4)
		self.matrix_6_entry.grid(row=2, column=2)
		self.matrix_7_entry = tkinter.Entry(self.matrix_entry, width=4)
		self.matrix_7_entry.grid(row=3, column=0)
		self.matrix_8_entry = tkinter.Entry(self.matrix_entry, width=4)
		self.matrix_8_entry.grid(row=3, column=1)
		self.matrix_9_entry = tkinter.Entry(self.matrix_entry, width=4)
		self.matrix_9_entry.grid(row=3, column=2)

		self.matrix_entry = tkinter.Frame(self.root)
		self.matrix_entry.place(relx=0.25, rely=0.3, anchor=tkinter.CENTER)

		self.enter_matrix_label = tkinter.Label(self.matrix_entry, text='Вектор-столбец')
		self.enter_matrix_label.grid(row=0, column=0, columnspan=4)

		self.matrix_10_entry = tkinter.Entry(self.matrix_entry, width=4)
		self.matrix_10_entry.grid(row=1, column=0)
		self.matrix_11_entry = tkinter.Entry(self.matrix_entry, width=4)
		self.matrix_11_entry.grid(row=2, column=0)
		self.matrix_12_entry = tkinter.Entry(self.matrix_entry, width=4)
		self.matrix_12_entry.grid(row=3, column=0)
  
		self.button = tkinter.Button(self.root, text='Вычислить', command=self.click)
		self.button.place(relx=0.09, rely=0.5, anchor=tkinter.CENTER)
  
		self.result = tkinter.Label(self.root, text='', font=('Arial', 10,'bold'))
		self.result.place(relx=0.15, rely=0.65, anchor=tkinter.CENTER)