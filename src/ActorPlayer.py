#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tabuleiro import Tabuleiro
from InterfaceGrafica import InterfaceGrafica
from tkinter import simpledialog
from tkinter import messagebox
from dog.dog_actor import DogActor
from dog.start_status import StartStatus
from dog.dog_interface import DogPlayerInterface
from random import randint
import time

class ActorPlayer(DogPlayerInterface):
	def __init__(self):
		self._gui : InterfaceGrafica = InterfaceGrafica(self)
		self._tabuleiro : Tabuleiro = Tabuleiro()

		player_name = simpledialog.askstring(title="Player identification", prompt="Qual o seu nome?")
		self._dog_server_interface = DogActor()
		message = self._dog_server_interface.initialize(player_name, self)
		messagebox.showinfo(message=message)

		self._gui._main_window.mainloop()
		

	def notificar(self, mensagem : str):
		messagebox.showinfo(message=mensagem)

	def start_match(self):
		start_status = self._dog_server_interface.start_match(2)
		code = start_status.get_code()
		message = start_status.get_message()

		if code == "0" or code == "1": #quando nao ha jogador suficiente
			messagebox.showinfo(message=message)
		else:#    (code=='2')
			self.reiniciarTabuleiro()
			jogadores = start_status.get_players()
			self._gui._label_nome1["text"] = jogadores[1][0]
			self._gui._label_nome2["text"] = jogadores[0][0]
			self._tabuleiro.iniciarTabuleiro(jogadores)
			if jogadores[0][2] == "1":
				messagebox.showinfo(message="Sua vez, rode o dado e posicione", title="Partida Iniciada")
			else:
				messagebox.showinfo(message="Vez do adversario, espere a jogada", title="Partida Iniciada")

	def clickTabuleiro(self, colunaSelecionada : int):
		fase = self._tabuleiro._ladoDoJogoLocal.pegaFase()
		if fase == "posicionar":
			colunaValida = self._tabuleiro.temVaga(colunaSelecionada)
			if colunaValida:
				a_move = {}
				self._tabuleiro.registraColunaSelecionadaLocal(colunaSelecionada)
				self._tabuleiro.registraDadoColunaSelecionadaLocal()
				coluna = colunaSelecionada + 7
				a_move["jogada"] = str(coluna)
				self.atualizarTabuleiro()
				self.verificarVencedor()
				andamento = self._tabuleiro.get_partida_andamento()
				if not andamento:
					a_move["match_status"] = "finished"
				else:
					a_move["match_status"] = "next"
				self._dog_server_interface.send_move(a_move)
			else:
				self.notificar("Coluna Inválida")


	def reiniciarTabuleiro(self):
		self._tabuleiro.reiniciarTabuleiro()
		self._gui.carregaInterface()

	def clickBotaoGirarDado(self):
		fase = self._tabuleiro._ladoDoJogoLocal.pegaFase()
		if fase == "lancarDado":
			a_move = {}
			dadoGirado = self.aleatorizarDado()
			self._tabuleiro.registrarDadoGiradoLocal(dadoGirado)
			self._gui.mostrarDadoGirado(dadoGirado, True)
			a_move["jogada"] = str(dadoGirado)
			a_move["match_status"] = "progress"
			self._dog_server_interface.send_move(a_move)

	def aleatorizarDado(self) -> int:
		return randint(1,6)

	def verificarVencedor(self):
		cheio = self._tabuleiro.verificarTabuleiroCheio()
		if cheio:
			vencedor = self._tabuleiro.quemGanhou()
			if vencedor == 0:	#Vencedor Local
				self._tabuleiro.setVitoriaLocal()
				time.sleep(1)
				self.notificar("Parabéns, você venceu!")
			elif vencedor == 1: #Vencedor Remoto
				self._tabuleiro.setVitoriaRemota()
				time.sleep(1)
				self.notificar("Você perdeu :(")
			else:
				time.sleep(1)
				self.notificar("Vocês empataram :O")
		else:	#NOT cheio
			self._tabuleiro.inverteTurnos()

	def receive_start(self, start_status : StartStatus):
		self.reiniciarTabuleiro()
		jogadores = start_status.get_players()
		self._gui._label_nome1["text"] = jogadores[1][0]
		self._gui._label_nome2["text"] = jogadores[0][0]
		self._tabuleiro.iniciarTabuleiro(jogadores)
		if jogadores[0][2] == "1":
			messagebox.showinfo(message="Sua vez, rode o dado e posicione", title="Partida Iniciada")
		else:
			messagebox.showinfo(message="Vez do adversario, espere a jogada", title="Partida Iniciada")

	def receive_withdrawal_notification(self):
		self.notificar("Adversário desistiu, você venceu!")

	def atualizarTabuleiro(self):
		turnoLocal = self._tabuleiro.checarTurnoLocal()
		if turnoLocal:
			dadoAtual = self._tabuleiro.verDadoAtualLocal()
			colunaAtual = self._tabuleiro.verColunaAtualLocal()
			existem = self._tabuleiro.verificarDadoIgualNoOponente(dadoAtual, colunaAtual)
			if existem:
				self._tabuleiro.destruirDadoOponente(dadoAtual, colunaAtual)
				dadosAtualizar = self._tabuleiro.pegarDadosColunaOponente(colunaAtual)
				self._gui.redesenharColunaOponente(dadosAtualizar, colunaAtual)
			self._gui.inserirDadoLocal(dadoAtual, colunaAtual)
		else:
			dadoAtual = self._tabuleiro.verDadoAtualRemoto()
			colunaAtual = self._tabuleiro.verColunaAtualRemoto()
			existem = self._tabuleiro.verificarDadoIgualNoLocal(dadoAtual, colunaAtual)
			if existem:
				self._tabuleiro.destruirDadoLocal(dadoAtual, colunaAtual)
				dadosAtualizar = self._tabuleiro.pegarDadosColunaLocal(colunaAtual)
				self._gui.redesenharColunaLocal(dadosAtualizar, colunaAtual)
			self._gui.inserirDadoOponente(dadoAtual, colunaAtual)
		self._tabuleiro.calcularPontuacao()
		pontuacaoColunasLocal = self._tabuleiro.pegarPontuacaoColunasLocal()
		pontuacaoColunasRemoto = self._tabuleiro.pegarPontuacaoColunasRemoto()
		pontuacaoTotalLocal = self._tabuleiro.pegarPontuacaoTotalLocal()
		pontuacaoTotalRemoto = self._tabuleiro.pegarPontuacaoTotalRemoto()
		self._gui.atualizarPontos(pontuacaoColunasLocal, pontuacaoTotalLocal, pontuacaoColunasRemoto, pontuacaoTotalRemoto)

	def receive_move(self, a_move : dict):
		jogada = int(a_move["jogada"])
		if jogada <= 6: #dado girado
			self._tabuleiro.registrarDadoGiradoRemoto(jogada)
			self._gui.mostrarDadoGirado(jogada, False)
		else: #coluna selecionada
			jogada -= 7
			self._tabuleiro.registraColunaSelecionadaRemota(jogada)
			self._tabuleiro.registraDadoColunaSelecionadaRemota()
			self.atualizarTabuleiro()
			self.verificarVencedor()



