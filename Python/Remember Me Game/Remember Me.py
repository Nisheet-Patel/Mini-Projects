try:
	import random
	import tkinter as TK
	from time import sleep
	import pygame
except:
	import os
	os.system("pip install pygame")
	os.system("python3 \"Remember Me.py\"")
pygame.init()

class _Game_:
	def __init__(self,masterr):
		self.masterr = masterr
		
		# - - Colors - - #
		self.bg_buttons = "#222222"
		self.yellow = "#ffde59"
		self.green = "#c9e265"
		self.blue = "#5ce1e6"
		self.orange = "#ff914d"

		# - - Score - - #
		self.nscore = 0

		# - - Variables - - #
		self.steps = []
		self.step_count = 0
		self.blink_speed = 0.5
		self.play_speed = 0.7

		# # #
		self.Create_file_log()
		self.First_page()

		# - - Import Sounds - - #
		
		try:
			self.select = pygame.mixer.Sound("Sounds/select.wav")
			self.enter_s = pygame.mixer.Sound("Sounds/enter.wav")
			self.game_over = pygame.mixer.Sound("Sounds/game-over.wav")

			self.Piano_sound()
			
		except: pass

	# - - Piano Sounds - - for Buttons - - #

	def Piano_sound(self):
		self.path = "Sounds/{}".format(random.randint(1,6))
		self.p1 = pygame.mixer.Sound("{}/p1.wav".format(self.path))
		self.p2 = pygame.mixer.Sound("{}/p2.wav".format(self.path))
		self.p3 = pygame.mixer.Sound("{}/p3.wav".format(self.path))
		self.p4 = pygame.mixer.Sound("{}/p4.wav".format(self.path))


	def Create_file_log(self):
		file = open("log.txt",'a+')
		file.close()

	def First_page(self):
		try:
			self.Destroy_last_page()
		except: pass
		self.f_canvas = TK.Canvas(self.masterr, width=500, height=100)
		self.f_canvas.create_rectangle(120,50,170,100, fill="#ffde59", outline="#ffde59")
		self.f_canvas.create_rectangle(190,50,240,100, fill="#c9e265", outline="#c9e265")
		self.f_canvas.create_rectangle(260,50,310,100, fill="#5ce1e6", outline="#5ce1e6")
		self.f_canvas.create_rectangle(330,50,380,100, fill="#ff914d", outline="#ff914d")
		self.f_canvas.pack()

		self.mtitle = TK.Label(self.masterr, text="Remember Me", font=("Gabriola",50,"bold"),fg="#222222")
		self.mtitle.pack()

		self.play_b = TK.Button(self.masterr, text="Play", font=("Copperplate Gothic", 25), width=10, padx=0, pady=0, relief="groove",bd=1,bg='white',fg="#222222", command=self.play_action)
		self.play_b.pack()

		self.play_b.bind("<Enter>",self.enter_play_b)
		self.play_b.bind("<Leave>",self.leave_play_b)

		self.copyright = TK.Label(text="©NN",font=("Gabriola", 20),fg="#222222")
		self.copyright.place(x=430,y=450)

	# - - Value Change for play button - - #

	def enter_play_b(self,e):
		self.select.play()
		self.play_b.config(fg="white", bg="#222222")
		
	def leave_play_b(self,e):
		self.play_b.config(fg="#222222", bg="white")


	# - - Play Button Action - - #
	
	def play_action(self):
		self.enter_s.play()
		try:
			self.Destroy_first_page()
			self.Destroy_last_page()
		except: pass
		self._Buttons_()
		self.genrate_step()
		tk.update()
		sleep(0.5)
		self.play_steps()

	# - - Game - - #

	def Get_best_score(self):
		file = open("log.txt",'r')
		rfile = file.readline()
		file.close()
		if str(rfile) != "":
			self.bs = int(rfile)
			return str(rfile)
		else:
			self.bs = 0
			return 0
		


	def Score(self):
		self.score = TK.Label(self.masterr, text="Score: {}".format(self.nscore), fg=self.bg_buttons, font=("Arial",15,"bold"), pady=20, padx=20)
		self.score.grid(row=0,column=0)

		self.best_score = TK.Label(self.masterr, text="Best Score: {}".format(self.Get_best_score()), fg=self.bg_buttons, font=("Arial",15,"bold"), pady=20, padx=210)
		self.best_score.grid(row=0,column=1)

	def _Buttons_(self):

		self.Score()

		self.button_frame = TK.Frame(self.masterr)

		self.b1 = TK.Button(self.button_frame, width=20, height=10, bg=self.bg_buttons, 
			relief="flat", activebackground=self.yellow, bd=0, command= lambda: self.Button_pressed(1),	
			state="normal")
		self.b1.grid(row=0, column=0, padx=10, pady=10)

		self.b2 = TK.Button(self.button_frame, width=20, height=10, bg=self.bg_buttons, 
			relief="flat", activebackground=self.green, bd=0, command= lambda: self.Button_pressed(2),	
			state="normal")
		self.b2.grid(row=0, column=1, padx=10, pady=10)

		self.b3 = TK.Button(self.button_frame, width=20, height=10, bg=self.bg_buttons, 
			relief="flat", activebackground=self.orange, bd=0, command= lambda: self.Button_pressed(3),	
			state="normal")
		self.b3.grid(row=1, column=0, padx=10, pady=10)

		self.b4 = TK.Button(self.button_frame, width=20, height=10, bg=self.bg_buttons, 
			relief="flat", activebackground=self.blue, bd=0, command= lambda: self.Button_pressed(4),	
			state="normal")
		self.b4.grid(row=1, column=1, padx=10, pady=10)

		self.button_frame.place(x=80,y=90)

	# - - Update's - - #

	def update_score(self):
		self.nscore += 1
		self.score.config(text="Score: {}".format(self.nscore))

	def disabled_buttons(self):				# disable buttons
		self.b1.config(state="disabled")
		self.b2.config(state="disabled")
		self.b3.config(state="disabled")
		self.b4.config(state="disabled")

	def active_buttons(self):				# active buttons
		self.b1.config(state="normal")
		self.b2.config(state="normal")
		self.b3.config(state="normal")
		self.b4.config(state="normal")

	def update_b1_color(self):
		self.b1.config(bg=self.yellow)
		self.p1.play()
		tk.update()
		sleep(self.blink_speed)
		self.b1.config(bg=self.bg_buttons)
		tk.update()

	def update_b2_color(self):
		self.b2.config(bg=self.green)
		self.p2.play()
		tk.update()
		sleep(self.blink_speed)
		self.b2.config(bg=self.bg_buttons)
		tk.update()

	def update_b3_color(self):
		self.b3.config(bg=self.orange)
		self.p3.play()
		tk.update()
		sleep(self.blink_speed)
		self.b3.config(bg=self.bg_buttons)
		tk.update()

	def update_b4_color(self):
		self.b4.config(bg=self.blue)
		self.p4.play()
		tk.update()
		sleep(self.blink_speed)
		self.b4.config(bg=self.bg_buttons)
		tk.update()

	# - - Algorithm - - #
	def Button_pressed(self,n):
		
		if n == 1:
			self.p1.play()
		elif n == 2:
			self.p2.play()
		elif n == 3:
			self.p3.play()
		elif n == 4:
			self.p4.play()

		if self.steps[self.step_count] != n:	# wrong Choice
			self.Piano_sound()
			self.game_over.play()
			self.Last_page()
		
		if len(self.steps)-1 == self.step_count:	
			self.step_count = -1
			self.update_score()
			if len(self.steps) == 1:
				tk.update()
				sleep(1)
			self.genrate_step()
			tk.update()
			sleep(self.play_speed)
			self.play_steps()
		self.step_count += 1

		self.write_best_score()		# Write Best score

	def genrate_step(self):
		self.steps.append(random.randint(1,4))

	
	def play_steps(self):
		self.disabled_buttons()
		for i in self.steps:
			sleep(0.15)
			if i == 1:
				self.update_b1_color()
			elif i == 2:
				self.update_b2_color()
			elif i == 3:
				self.update_b3_color()
			elif i == 4:
				self.update_b4_color()
		self.active_buttons()

	# - Write Best Score - - #

	def write_best_score(self):
		if self.bs < self.nscore:
			file = open("log.txt",'w')
			file.truncate()
			file.write("{}".format(self.nscore))
			file.close()
			self.Get_best_score()
		if self.nscore == 10:
			self.play_speed -= 0.1
		if self.nscore == 15:
			self.play_speed -= 0.1
		if self.nscore == 20:
			self.play_speed -= 0.1
		if self.nscore == 30:
			self.play_speed -= 0.2
			self.blink_speed -= 0.1
	# - - Last Page - - #

	def Last_page(self):

		self.Destroy_game()

		self.l_canvas = TK.Canvas(self.masterr, width=500, height=100)
		self.l_canvas.create_rectangle(120,50,170,100, fill=self.bg_buttons, outline="#ffde59")
		self.l_canvas.create_rectangle(190,50,240,100, fill=self.bg_buttons, outline="#c9e265")
		self.l_canvas.create_rectangle(260,50,310,100, fill=self.bg_buttons, outline="#5ce1e6")
		self.l_canvas.create_rectangle(330,50,380,100, fill=self.bg_buttons, outline="#ff914d")
		self.l_canvas.pack()

		self.ltitle = TK.Label(self.masterr, text="You Don't\nRemember Me \n:(", font=("Gabriola",35,"bold"),fg="#222222")
		self.ltitle.pack()

		self.play_again_b = TK.Button(self.masterr, text="Play Again", font=("Copperplate Gothic", 20), width=10, padx=0, pady=0, relief="groove",bd=1,bg='white',fg="#222222", command=self.play_action)
		self.play_again_b.pack(side="left",padx=20, pady=40)

		self.home_b = TK.Button(self.masterr, text="Home", font=("Copperplate Gothic", 20), width=10, padx=0, pady=0, relief="groove",bd=1,bg='white',fg="#222222", command=self.home_b_action)
		self.home_b.pack(side="right",padx=20, pady=40)

		self.play_again_b.bind("<Enter>",self.enter_play_again_b)
		self.play_again_b.bind("<Leave>",self.leave_play_again_b)

		self.home_b.bind("<Enter>",self.enter_home_b)
		self.home_b.bind("<Leave>",self.leave_home_b)

	def home_b_action(self):
		self.enter_s.play()
		self.First_page()

	# - - Value Change for play Again button - - #

	def enter_play_again_b(self,e):
		self.select.play()
		self.play_again_b.config(fg="white", bg="#222222")

	def leave_play_again_b(self,e):
		self.play_again_b.config(fg="#222222", bg="white")
	
	def enter_home_b(self,e):
		self.select.play()
		self.home_b.config(fg="white", bg="#222222")

	def leave_home_b(self,e):
		self.home_b.config(fg="#222222", bg="white")



	
	# - - Destroy - - #

	def Destroy_first_page(self):
		self.f_canvas.destroy()
		self.mtitle.destroy()
		self.play_b.destroy()
	
	def Destroy_last_page(self):
		self.l_canvas.destroy()
		self.ltitle.destroy()
		self.play_again_b.destroy()
		self.home_b.destroy()
		self.write_best_score()		# Write Best score
		self.step_count = 0
		self.steps.clear()
		self.nscore = 0

	def Destroy_game(self):
		self.button_frame.destroy()
		self.score.destroy()
		self.best_score.destroy()



if __name__ == '__main__':
		
	tk = TK.Tk()
	tk.geometry("500x500")
	tk.maxsize(500,500)
	tk.minsize(500,500)

	try:
		tk.iconbitmap("iocn_.ico")
	except: pass

	tk.title("Remember Me | ©NN")
	game = _Game_(tk)

	tk.mainloop()
	