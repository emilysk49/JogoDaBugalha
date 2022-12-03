#!/usr/bin/python
# -*- coding: UTF-8 -*-
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
from dog.dog_actor import DogActor

class InterfaceGrafica():
	def __init__(self, actor):
		self._main_window : Tk = Tk()
		self._main_window.title("Jogo da Bugalha")
		self._main_window.iconbitmap("images/icon.ico")
		self._main_window.geometry("550x980")
		self._main_window.resizable(False, False)
		self._main_window["bg"]= "gray"

		self._tabuleiro_frame = Frame(self._main_window, padx=30, pady=30, bg="gray")
		self._dado_frame : Frame = Frame(self._main_window, padx=32, bg="gray")

		self._empty : PhotoImage = PhotoImage(file="images/empty.gif")
		self._dado0 : PhotoImage = PhotoImage(file="images/dado0.gif")
		self._dado1 : PhotoImage = PhotoImage(file="images/dado1.gif")
		self._dado2 : PhotoImage = PhotoImage(file="images/dado2.gif")
		self._dado3 : PhotoImage = PhotoImage(file="images/dado3.gif")
		self._dado4 : PhotoImage = PhotoImage(file="images/dado4.gif")
		self._dado5 : PhotoImage = PhotoImage(file="images/dado5.gif")
		self._dado6 : PhotoImage = PhotoImage(file="images/dado6.gif")
		self._label_tabuleiro : list = [] #Label's
		self._label_dado1 : Label = None
		self._label_dado2 : Label = None
		self._label_pTotal1 : Label = None
		self._label_pTotal2 : Label = None
		self._label_nome1 : Label = None
		self._label_nome2 : Label = None
		self._actorPlayer = actor

		self._menubar = Menu(self._main_window)
		self._menubar.option_add("*tearOff", FALSE)
		self._main_window["menu"] = self._menubar
		self._menu_file = Menu(self._menubar)
		self._menubar.add_cascade(menu=self._menu_file, label="Menu")
		self._menu_file.add_command(label="Iniciar jogo", command=self._actorPlayer.start_match)


		for y in range(3):
			a_column = []
			for x in range(8):
				if x != 3 and x != 4:
					aLabel = Label(self._tabuleiro_frame, bd=2, image=self._empty, bg="gray21")
					aLabel.grid(row=x, column=y)
					if x > 4:
						aLabel.bind(
							"<Button-1>", lambda event, column=y: self._actorPlayer.clickTabuleiro(column)
						)
				else:
					aLabel = Label(self._tabuleiro_frame, text="0", pady=30, bg="gray", fg="white", font=("_", 20))
					aLabel.grid(row=x, column=y)
				a_column.append(aLabel)
			self._label_tabuleiro.append(a_column)


		self._label_pTotal1 = Label(self._dado_frame, text="0", bg="gray", pady=30, fg="white", font=("_", 25))
		self._label_pTotal1.grid(row=0, column=0)

		self._label_dado1 = Label(self._dado_frame, bg="gray", image=self._dado0)
		self._label_dado1.grid(row=1, column=0)

		self._label_nome1 = Label(self._dado_frame, text="", bg="gray", pady=30, fg="white", font=("_", 25))
		self._label_nome1.grid(row=2, column=0, pady=(0,300))

		self._label_dado2 = Label(self._dado_frame, bg="gray", image=self._dado0, pady=50)
		self._label_dado2.grid(row=4, column=0)
		self._label_dado2.bind(
			"<Button-1>", lambda event: self._actorPlayer.clickBotaoGirarDado()
		)
		self._label_pTotal2 = Label(self._dado_frame,  text="0", bg="gray", pady=30, fg="white", font=("_", 25))
		self._label_pTotal2.grid(row=3, column=0)

		self._label_nome2 = Label(self._dado_frame, text="", bg="gray", pady=30, fg="white", font=("_", 25))
		self._label_nome2.grid(row=5, column=0)

		self._dado_frame.grid(row=0, column=1)
		self._tabuleiro_frame.grid(row=0, column=0)

		#################################################################################################################################

	

	def mostrarDadoGirado(self, dadoGirado : int, ehDadoLocal : bool):
		if ehDadoLocal:
			self._label_dado2.config(image=getattr(self, '_dado'+ str(dadoGirado)))
		else:
			self._label_dado1.config(image=getattr(self, '_dado'+ str(dadoGirado)))

	def redesenharColunaOponente(self, dadosAtualizar : list, colunaAtual : int):
		for i in range(3): #percorre a coluna de cima para baixo
			if dadosAtualizar[i] == -1:
				self._label_tabuleiro[colunaAtual][2-i]["imag"] = self._empty
			else:
				self._label_tabuleiro[colunaAtual][2-i]["imag"] = getattr(self, '_dado'+ str(dadosAtualizar[i]))
				

	def atualizarPontos(self, pontuacaoColunasLocal : list, pontuacaoTotalLocal : int, pontuacaoColunasRemoto : list, pontuacaoTotalRemoto : int):
		for i in range(3):
			for u in range(2):
				if u == 0:
					self._label_tabuleiro[i][3+u]["text"] = str(pontuacaoColunasRemoto[i])
				else:
					self._label_tabuleiro[i][3+u]["text"] = str(pontuacaoColunasLocal[i])

		self._label_pTotal1["text"] = str(pontuacaoTotalRemoto)
		self._label_pTotal2["text"] = str(pontuacaoTotalLocal)


	def redesenharColunaLocal(self, dadosAtualizar : list, colunaAtual : int):
		for i in range(3): #percorre a coluna de cima para baixo
			if dadosAtualizar[i] == -1:
				self._label_tabuleiro[colunaAtual][5+i]["imag"] = self._empty
			else:
				self._label_tabuleiro[colunaAtual][5+i]["imag"] = getattr(self, '_dado'+ str(dadosAtualizar[i]))

	def inserirDadoLocal(self, dadoAtual : int, colunaAtual : int):
		for i in range(3):
			if self._label_tabuleiro[colunaAtual][5+i]["imag"] == "pyimage1":
				self._label_tabuleiro[colunaAtual][5+i]["imag"] = getattr(self, '_dado'+ str(dadoAtual))
				break
		self._label_dado2["imag"] = self._dado0


	def inserirDadoOponente(self, dadoAtual : int, colunaAtual : int):
		for i in range(3):
			if self._label_tabuleiro[colunaAtual][2-i]["imag"] == "pyimage1":
				self._label_tabuleiro[colunaAtual][2-i]["imag"] = getattr(self, '_dado'+ str(dadoAtual))
				break
		self._label_dado1["imag"] = self._dado0


	#Ele carrega uma interface padrão com tudo zerado
	def carregaInterface(self):
		self._label_dado1["imag"] = self._dado0
		self._label_dado2["imag"] = self._dado0
		self._label_pTotal1["text"] = str(0)
		self._label_pTotal2["text"] = str(0)
		for i in range(3):
			for j in range(8):
				if j != 3 and j != 4:
					self._label_tabuleiro[i][j]["imag"] = self._empty
				else:
					self._label_tabuleiro[i][j]["text"] = "0"

