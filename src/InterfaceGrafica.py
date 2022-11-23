#!/usr/bin/python
# -*- coding: UTF-8 -*-
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
from DOG.dog_actor import DogActor

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
					aLabel = Label(self._tabuleiro_frame, bd=2, image=self._empty)
					aLabel.grid(row=x, column=y)
					if x > 4:
						aLabel.bind(
							"<Button-1>", lambda event, column=y: self._actorPlayer.clickTabuleiro(column)
						)
				else:
					aLabel = Label(self._tabuleiro_frame, text="Num", pady=30, bg="gray", font=("_", 20))
					aLabel.grid(row=x, column=y)
				a_column.append(aLabel)
			self._label_tabuleiro.append(a_column)

		self._label_dado1 = Label(self._dado_frame, bg="gray", image=self._dado0)
		self._label_dado1.grid(row=0, column=0, pady=(0,370))
		self._label_dado2 = Label(self._dado_frame, bg="gray", image=self._dado0, pady=50)
		self._label_dado2.grid(row=1, column=0)
		self._label_dado2.bind(
			"<Button-1>", lambda event: self._actorPlayer.clickBotaoGirarDado()
		)

		self._dado_frame.grid(row=0, column=1)
		self._tabuleiro_frame.grid(row=0, column=0)

		#################################################################################################################################
		

	def desabilitaColunas(self):
		pass

	def notificar(self, mensagem : str):
		pass

	def desabilitaGirarDado(self):
		pass

	def mostrarDadoGirado(self, dadoGirado : int, ehDadoLocal : bool):
		pass

	def habilitarColunas(self):
		pass

	def redesenharColunaOponente(self, *dadosAAtualizar : int, colunaAtual : int):
		pass

	def inserirDadoLocal(self, dadoAtual : int, colunaAtual : int):
		pass

	def atualizarPontos(self, pontuacaoColunasLocal : list, pontuacaoTotalLocal : int, pontuacaoColunasRemoto : list, pontuacaoTotalRemoto : int):
		pass

	def habilitarGirarDado(self):
		pass

	def redesenharColunaLocal(self, dadosAAtualizar : list, colunaAtual : int):
		pass

	def inserirDadoOponente(self, dadoAtual : int, colunaAtual : int):
		pass

	def carregaInterface(self):
		pass

