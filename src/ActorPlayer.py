#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tabuleiro import Tabuleiro
from InterfaceGrafica import InterfaceGrafica
from tkinter import simpledialog
from tkinter import messagebox
from DOG.dog_actor import DogActor
from DOG.start_status import StartStatus
from DOG.dog_interface import DogPlayerInterface
from random import randint

class ActorPlayer(DogPlayerInterface):
	def __init__(self):
		self._gui : InterfaceGrafica = InterfaceGrafica(self)
		self._tabuleiro : Tabuleiro = Tabuleiro()

		player_name = simpledialog.askstring(title="Player identification", prompt="Qual o seu nome?")
		self._dog_server_interface = DogActor()
		message = self._dog_server_interface.initialize(player_name, self)
		messagebox.showinfo(message=message)

		self._gui._main_window.mainloop()
		

	def selecionarPosicao(self, colunaSelecionada : int):
		pass

	def notificar(self, mensagem : str):
		pass

	def start_match(self):
		start_status = self._dog_server_interface.start_match(2)
		code = start_status.get_code()
		message = start_status.get_message()

		if code == "0" or code == "1": #quando nao ha jogador
			messagebox.showinfo(message=message)
		else:#    (code=='2')
			self.reiniciarTabuleiro()
			jogadores = start_status.get_players()
			self._tabuleiro.iniciarTabuleiro(jogadores)
			messagebox.showinfo(message=message)


	def clickTabuleiro(self, colunaSelecionada : int):
		if self._tabuleiro._ladoDoJogoLocal._fase == "posicionar":
			colunaValida = self._tabuleiro.temVaga(colunaSelecionada)
			if colunaValida:
				a_move = {}
				self._tabuleiro.registraColunaSelecionada(colunaSelecionada)
				self._tabuleiro.registraDadoColunaSelecionada()
				self.atualizarTabuleiro()
				coluna = colunaSelecionada + 6
				a_move["jogada"] = str(coluna)
				a_move["match_status"] = "progress"
				self._dog_server_interface.send_move(a_move)
				self.verifcarVencedor()
			else:
				self._gui.notificar("Coluna Inválida")


	def reiniciarTabuleiro(self):
		self._tabuleiro.reiniciarTabuleiro()
		self._gui.carregaInterface()

	def clickBotaoGirarDado(self):
		if self._tabuleiro._ladoDoJogoLocal._fase == "lancarDado":
			print("CLICOU")
			a_move = {}
			#self._gui.desabilitaGirarDado() PODEMOS TIRAR 
			dadoGirado = self.aleatorizarDado()
			self._tabuleiro.registrarDadoGirado(dadoGirado)
			self._gui.mostrarDadoGirado(dadoGirado, True)
			a_move["jogada"] = str(dadoGirado)
			a_move["match_status"] = "progress"
			self._dog_server_interface.send_move(a_move)

	def aleatorizarDado(self) -> int:
		return randint(1,6)

	def verifcarVencedor(self):
		pass

	def receive_start(self, start_status : StartStatus):
		self.reiniciarTabuleiro()
		jogadores = start_status.get_players()
		message = start_status.get_message()
		self._tabuleiro.iniciarTabuleiro(jogadores)
		#self.reiniciarTabuleiro() #precisa ocorrer dentro de iniciar partida
		messagebox.showinfo(message=message)

	def receive_withdrawal_notification(self):
		pass

	def atualizarTabuleiro(self):
		turnoLocal = self._tabuleiro.checarTurnoLocal()
		if turnoLocal:
			dadoAtual = self._tabuleiro.verDadoAtualLocal()
			colunaAtual = self._tabuleiro.verColunaAtualLocal()
			existem = self._tabuleiro.verificarDadoIgualNoOponente(dadoAtual, colunaAtual)
			if existem:
				self._tabuleiro.destruirDadoOponente(dadoAtual, colunaAtual)
			dadosAtualizar = self._tabuleiro.pegarDadosColunaOponente()
			self._gui.redesenharColunaOponente(dadosAtualizar, colunaAtual)
			self._gui.inserirDadoLocal(dadoAtual, colunaAtual)
		else:
			dadoAtual = self._tabuleiro.verDadoAtualRemoto()
			colunaAtual = self._tabuleiro.verColunaAtualRemoto()
			existem = self._tabuleiro.verificarDadoIgualNoLocal(dadoAtual, colunaAtual)
			if existem:
				self._tabuleiro.destruirDadoLocal(dadoAtual, colunaAtual)
			dadosAtualizar = self._tabuleiro.pegarDadosColunaLocal()
			self._gui.redesenharColunaLocal(dadosAtualizar, colunaAtual)
			self._gui.inserirDadoOponente(dadoAtual, colunaAtual)
		self._tabuleiro.calcularPontuacao()
		pontuacaoColunasLocal = self._tabuleiro.pegarPontuacaoColunasLocal()
		pontuacaoColunasRemoto = self._tabuleiro.pegarPontuacaoColunasRemoto()
		pontuacaoTotalLocal = self._tabuleiro.pegarPontuacaoTotalLocal()
		pontuacaoTotalRemoto = self._tabuleiro.pegarPontuacaoTotalRemoto()
		self._gui.atualizarPontos(pontuacaoColunasLocal, pontuacaoTotalLocal, pontuacaoColunasRemoto, pontuacaoTotalRemoto)

	def receive_move(self, a_move : dict):
		pass

