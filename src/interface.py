from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor
import random


class ActorPlayer(DogPlayerInterface):
	def __init__(self):
		self.main_window = Tk()
		self.fill_main_window()

		################################ implementacao para entrega 2 ################################
		player_name = simpledialog.askstring(title="Player identification", prompt="Qual o seu nome?")
		self.dog_server_interface = DogActor()
		message = self.dog_server_interface.initialize(player_name, self)
		messagebox.showinfo(message=message)
		################################################################################################

		self.main_window.mainloop()


	def fill_main_window(self):
		self.main_window.title("Jogo da Bugalha")
		self.main_window.iconbitmap("images/icon.ico")
		self.main_window.geometry("550x980")
		self.main_window.resizable(False, False)
		self.main_window["bg"]= "gray"

		self.tabuleiro_frame = Frame(self.main_window, padx=30, pady=30, bg="gray")

		self.dado_frame = Frame(self.main_window, padx=32, bg="gray")

		self.empty = PhotoImage(file="images/empty.gif")		
		self.dado1 = PhotoImage(file="images/dado1.gif")
		self.dado2 = PhotoImage(file="images/dado2.gif")
		self.dado3 = PhotoImage(file="images/dado3.gif")
		self.dado4 = PhotoImage(file="images/dado4.gif")
		self.dado5 = PhotoImage(file="images/dado5.gif")
		self.dado6 = PhotoImage(file="images/dado6.gif")

		self.menubar = Menu(self.main_window)
		self.menubar.option_add("*tearOff", FALSE)
		self.main_window["menu"] = self.menubar
		self.menu_file = Menu(self.menubar)
		self.menubar.add_cascade(menu=self.menu_file, label="Menu")
		self.menu_file.add_command(label="Iniciar jogo", command=self.start_match)
		#self.menu_file.add_command(label="Reiniciar", command=self.start_game)

		self.board_view = []
		for y in range(3):
			a_column = []
			for x in range(8):
				if x != 3 and x != 4:
					aLabel = Label(self.tabuleiro_frame, bd=2, image=self.empty)
					aLabel.grid(row=x, column=y)
					if x > 4:
						aLabel.bind(
							"<Button-1>", lambda event, line=x, column=y: self.click(event, line, column)
						)
				else:
					aLabel = Label(self.tabuleiro_frame, text="Num", pady=30, bg="gray", font=("_", 20))
					aLabel.grid(row=x, column=y)
				a_column.append(aLabel)
			self.board_view.append(a_column)

		
		self.dado_atual1 = self.aleatrizarDado()
		self.dado_atual2 = self.aleatrizarDado()
		self.label_dado1 = Label(self.dado_frame, bg="gray", image=getattr(self, 'dado'+self.dado_atual1))
		self.label_dado1.grid(row=0, column=0, pady=(0,370))
		self.label_dado2 = Label(self.dado_frame, bg="gray", image=getattr(self, 'dado'+self.dado_atual2), pady=50)
		self.label_dado2.grid(row=1, column=0)

		
		self.dado_frame.grid(row=0, column=1)
		self.tabuleiro_frame.grid(row=0, column=0)

	def aleatrizarDado(self):
		return str(random.randint(1,6))


	def click(self, event, linha, coluna):
		label=self.board_view[coluna][linha]
		if label['imag']=='pyimage1':
			label['imag']=getattr(self, 'dado'+self.dado_atual2)
			self.dado_atual2 = self.aleatrizarDado()
			self.label_dado2.configure(image=getattr(self, 'dado'+self.dado_atual2))

	def start_match(self):
		#quantidade de jogadores (2) para iniciar jogo
		start_status = self.dog_server_interface.start_match(2)
		message = start_status.get_message()
		messagebox.showinfo(message=message)

	def receive_start(self, start_status):
		message = start_status.get_message()
		messagebox.showinfo(message=message)

	def receive_withdrawal_notification(self):
		message = "Adversário desconectou."
		messagebox.showinfo(message=message)
	

ActorPlayer()

        