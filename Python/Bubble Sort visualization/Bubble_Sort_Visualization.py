import tkinter as tk
from time import sleep

class Bubble_Sort:
	def __init__(self,masterr):
		self.masterr = masterr
		self.array_list = list()
		self.index_list = list()
		self.value = list()
		self.Step_recored = list()

		# -- Visual Control -- #
		self.visualize = True
		self.slow =1.2
		# -- Run Control -- #
		self.running = False
		self.cu_pos = 0
		# -- Next Control --#
		self.previous = False
		self.g = 1

	def add_to_box(self,l):
		for i in range(len(l)):
			self.array_list[i].insert(0,"{}".format(l[i]))

	def create_value_list(self):
		for i in self.array_list:
			if i.get() == "":
				self.value.append(0)
			else:
				self.value.append(int(i.get()))
		return self.value

	def Clear_colors(self,n):
		try:
			for i in range(n):
				self.array_list[i].config(bg='#ffffff')
		except: pass

	def Orange(self,n):
		try:
			self.array_list[n].config(bg="#FDCB7F")
		except: pass
	
	def Blue(self,n):
		try:
			self.array_list[n].config(bg="#7FEDFD")
		except: pass

	def Green(self,n):
		try:
			self.array_list[n].config(bg="#BEFD7F")
		except: pass

	def File_edit(self):
		file = open("log.txt",'r+')
		k = 0
		
		rfile = file.readlines()
		try:         
			for i in rfile:
				print(i,k)
				self.Step_recored[k][2] = eval(i.removesuffix("\n"))
				k += 1
		except: pass
		file.close()

	def Bubble_Sort(self):
		print("BS",self.running)
		self.Step_recored.clear()
		if not self.running:
			self.running = True
			NList = self.create_value_list()
			if sum(NList) > 0:
				print("BS-SUM",sum(NList))
				self.cu_pos = 0
				self.g = 1
				file = open("log.txt",'w+')
				file.truncate()
				self.nextprev()
				self.Step_recored.clear()
				for i in range(len(NList)):
					flag = 0
					for j in range(len(NList)-i-1):
						file.write(f"{NList}\n")
						self.Step_recored.append([j,j+1,0])
						if NList[j] > NList[j+1]:
							NList[j],NList[j+1] = NList[j+1], NList[j]
							
							file.write(f"{NList}\n")
							self.Step_recored.append([j+1,j,0])
							flag += 1
					print(NList)
						
					if flag == 0: break
				file.close()
				self.File_edit()
			self.running = False
			self.value.clear()
			print(self.Step_recored)


	def PlayBubbleSort(self):
		try:
			self.start_b.destroy()
			self.end_b.destroy()
			self.next_b.destroy()
			self.previous_b.destroy()
		except: pass
		print("PBS",self.running)
		if not self.running:
			self.running = True
			NList = self.create_value_list()
			if sum(NList) > 0:
				self.stop = False
				self.clear_b.config(text="Stop",command=self.stop_)
				for i in range(len(NList)):
					if not self.stop:
						flag = 0
						for j in range(len(NList)-i-1):
							if not self.stop:
								self.Clear_colors(len(NList)-i)
								self.Blue(j)
								self.Orange(j+1)
								self.masterr.update()
								sleep(self.slow)
								if NList[j] > NList[j+1]:
									NList[j],NList[j+1] = NList[j+1], NList[j]

									self.array_list[j].delete(0,tk.END)
									self.array_list[j+1].delete(0,tk.END)
									
									self.array_list[j].insert(0,"{}".format(NList[j]))
									self.array_list[j+1].insert(0,"{}".format(NList[j+1]))
									print(j,j+1,NList[j],NList[j+1])
									self.Blue(j+1)
									self.Orange(j)
									self.masterr.update()
									sleep(1.2)

									flag += 1
						self.Green(len(NList)-i-1)
						self.masterr.update()
						print(i,NList,flag)
						if flag == 0: break
				for i in self.array_list:
					i.config(bg="#BEFD7F")
				self.clear_b.config(text="clear",command=self.clear_value)
			self.running = False
	
	def stop_(self):
		self.stop = True
		self.running = False
		self.value.clear()
		NList = self.create_value_list()
		for i in range(len(NList)):
			for j in range(len(NList)-i-1):
				if NList[j] > NList[j+1]:
					NList[j],NList[j+1] = NList[j+1], NList[j]
		for k in range(len(self.array_list)):
			self.array_list[k].delete(0,tk.END)
			self.array_list[k].insert(0,"{}".format(NList[k]))
		for i in self.array_list:
			i.config(bg="#BEFD7F")	
		self.clear_b.config(text="clear",command=self.clear_value)


	def clear_value(self):
		self.value.clear()
		self.stop = False
		self.running = False
		for i in self.array_list:
			i.delete(0,tk.END)
		self.Clear_colors(len(self.array_list))
		try:
			self.start_b.destroy()
			self.end_b.destroy()
			self.next_b.destroy()
			self.previous_b.destroy()
		except: pass
		self.Step_recored.clear()
		self.Clear_colors(len(self.array_list))
		file = open("log.txt",'w')
		file.close()


	def delete_boxs(self):
		try:
			for i in self.array_list:
				i.destroy()
		except:pass
		try:
			for i in self.index_list:
				i.destroy()
		except: pass	

	def Genrate_array(self,n):
		try:
			self.play_sorted_b.destroy()
			self.clear_b.destroy()
			self.sorted_b.destroy()
		except: pass	
		
		self.delete_boxs()

		box_frame = tk.Frame(self.masterr)
		box_frame.place(x=5,y=50)
		self.array_list.clear()
		self.value.clear()
		self.index_list.clear()

		

		h = 200
		w = 0

		for i in range(n):
			self.index_l = tk.Label(box_frame,text=f"{i}")
			self.index_l.grid(row=0,column=i)
			self.index_list.append(self.index_l)
			self.entry = tk.Entry(box_frame, width=2, font=("Helvetica",30), bg="#ffffff", relief="ridge")
			self.array_list.append(self.entry)
			self.entry.grid(row=1,column=i,padx=1)
			self.masterr.update()
			w += 52

		if w < 260: w = 260

		self.play_sorted_b = tk.Button(box_frame, text="Play Bubble Sort", command=self.PlayBubbleSort)
		self.play_sorted_b.grid(row=2, column=0, pady=10, columnspan=2)
		self.clear_b = tk.Button(box_frame, text="Clear", command=self.clear_value)
		self.clear_b.grid(row=2, column=4, pady=10)
		self.sorted_b = tk.Button(box_frame, text="Bubble Sort", command=self.Bubble_Sort)
		self.sorted_b.grid(row=2, column=2, pady=10, columnspan=2)
		root.geometry(f"{w}x{h}")

	def Clear_box_value(self):
		try:
			for i in self.array_list:
				i.delete(0,tk.END)
		except: pass

	def NEXT(self):
		if self.cu_pos < 0: self.cu_pos = 0		
		if self.cu_pos < len(self.Step_recored):
			print(self.cu_pos)
			# -- Clear all Color box --# 
			try:
				self.Clear_colors(len(self.array_list))
			except: pass


			self.Blue(int(self.Step_recored[self.cu_pos][0]))
			self.Orange(int(self.Step_recored[self.cu_pos][1]))

			self.Clear_box_value()
			self.add_to_box(self.Step_recored[self.cu_pos][2])

			self.cu_pos += 1
		else:
			for i in range(len(self.array_list)):
				self.Green(i)	

	def PREVIOUS(self):
		self.cu_pos -= 1
		if (self.cu_pos-1) == -1 or (self.cu_pos-1) < 0: self.cu_pos = 1

		if self.cu_pos < len(self.Step_recored) or self.cu_pos > -1:	
			print(self.cu_pos-1)
			# -- Clear all Color box --# 
			try:
				self.Clear_colors(len(self.array_list))
			except: pass


			self.Blue(int(self.Step_recored[self.cu_pos-1][0]))
			self.Orange(int(self.Step_recored[self.cu_pos-1][1]))

			self.Clear_box_value()
			self.add_to_box(self.Step_recored[self.cu_pos-1][2])

			
	def l0(self):
		self.Clear_box_value()
		# -- Clear all Color box --# 
		try:
			self.Clear_colors(len(self.array_list))
		except: pass

		self.add_to_box(self.Step_recored[0][2])

	def l1(self):
		self.Clear_box_value()
		for i in range(len(self.array_list)):
			self.Green(i)	
			
		self.add_to_box(self.Step_recored[-1][2])


	def nextprev(self):
		self.start_b = tk.Button(self.masterr, text="0", command=self.l0)
		self.start_b.place(x=90, y=160)
		self.end_b = tk.Button(self.masterr, text="1", command=self.l1)
		self.end_b.place(x=210, y=160)
		self.next_b = tk.Button(self.masterr, text="Next", command=self.NEXT)
		self.next_b.place(x=170, y=160)
		self.previous_b = tk.Button(self.masterr, text="Previous", command=self.PREVIOUS)
		self.previous_b.place(x=110, y=160)

	def len_array_entry(self):
		self.arra_range_l = tk.Label(self.masterr, text="Array Range:",font=("Helvetica",10))
		self.arra_range_l.grid(row=0, column=0,pady=10,sticky=tk.NE)

		self.len_array_e = tk.Entry(self.masterr, width=4,font=("Helvetica",15), bg="#ffffff", relief="ridge")
		self.len_array_e.grid(row=0, column=1,pady=10,padx=2,sticky=tk.NE)

		self.len_array_e.bind("<Return>", lambda e: self.Genrate_array(int(self.len_array_e.get())))

		self.abutton = tk.Button(self.masterr, text="Generate", command=lambda: self.Genrate_array(int(self.len_array_e.get())))
		self.abutton.grid(row=0, column=2,pady=10,sticky=tk.NE, padx=2)

if __name__ == '__main__':
	root = tk.Tk()
	root.geometry("300x70")
	root.title("Bubble Sort Visualization | ©NN")
	try:
		root.iconbitmap("Bubble_ico.ico")
	except: pass
	GUI = Bubble_Sort(root)
	GUI.len_array_entry()

	root.mainloop()
