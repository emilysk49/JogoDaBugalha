#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tabuleiro import Tabuleiro
from InterfaceGrafica import InterfaceGrafica
from tkinter import simpledialog
from tkinter import messagebox
from DOG.dog_actor import DogActor
from DOG.start_status import StartStatus
from DOG.dog_interface import DogPlayerInterface

class ActorPlayer(DogPlayerInterface):
	def __init__(self):
		self._gui : InterfaceGrafica = InterfaceGrafica(self)
		self._tabuleiro : Tabuleiro = Tabuleiro()

		self._gui.carregaInterface()

		player_name = simpledialog.askstring(title="Player identification", prompt="Qual o seu nome?")
		self.dog_server_interface = DogActor()
		message = self.dog_server_interface.initialize(player_name, self)
		messagebox.showinfo(message=message)

		self._gui._main_window.mainloop()
		

	def selecionarPosicao(self, colunaSelecionada : int):
		pass

	def notificar(self, mensagem : str):
		pass

	def start_match(self):
		pass

	def clickTabuleiro(self, colunaSelecionada : int):
		print("Clickou na coluna %d" % colunaSelecionada)

	def reiniciarTabuleiro(self):
		pass

	def clickBotaoGirarDado(self):
		print("Clickou no Botao")

	def aleatorizarDado(self) -> int:
		pass

	def verifcarVencedor(self):
		pass

	def receive_start(self, start_status : StartStatus):
		pass

	def start_game(self):
		pass

	def receive_withdrawal_notification(self):
		pass

	def atualizarTabuleiro(self):
		pass

	def receive_move(self, a_move : dict):
		pass

