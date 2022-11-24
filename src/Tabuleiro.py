#!/usr/bin/python
# -*- coding: UTF-8 -*-
from LadoDeJogo import LadoDeJogo

class Tabuleiro():
	def __init__(self):
		self._partida_andamento : bool = False
		self._ladoDoJogoLocal : LadoDeJogo = LadoDeJogo()
		self._ladoDoJogoRemoto : LadoDeJogo = LadoDeJogo()


	def iniciarTabuleiro(self, jogadores : list):
		jogadorLocal_nome = jogadores[0][0]
		jogadorLocal_id = jogadores[0][1]
		jogadorLocal_order = jogadores[0][2]
		jogadorRemoto_nome = jogadores[1][0]
		jogadorRemoto_id = jogadores[1][1]
		self._ladoDoJogoLocal.inicializar(jogadorLocal_id, jogadorLocal_nome)
		self._ladoDoJogoRemoto.inicializar(jogadorRemoto_id, jogadorRemoto_nome)

		self.partidaEmAndamento()

		if jogadorLocal_order == "1": #Vez do jogadorLocal
			print("vc comeca")
			self._ladoDoJogoLocal.inverteTurno()
		else:
			print("vc espera")
			self._ladoDoJogoRemoto.inverteTurno()


	def temVaga(self, colunaSelecionada : int) -> bool:
		return self._ladoDoJogoLocal.temVaga(colunaSelecionada)

	def registraColunaSelecionada(self, colunaSelecionada : int):
		self._ladoDoJogoLocal(colunaSelecionada)

	def registraDadoColunaSelecionada(self):
		self._ladoDoJogoLocal()

	def reiniciarTabuleiro(self):
		self._ladoDoJogoLocal.limparColunas()
		self._ladoDoJogoRemoto.limparColunas()

	def registrarDadoGirado(self, dadoGirado : int):
		self._ladoDoJogoLocal.registraDadoGirado(dadoGirado)

	def verificarTabuleiroCheio(self) -> bool:
		pass

	def quemGanhou(self) -> int:
		pass

	def calcularPontuacao(self):
		pass

	def partidaEmAndamento(self):
		self._partida_andamento = True

	def fimPartida(self):
		self._partida_andamento = False

	def checarTurnoLocal(self) -> bool:
		pass

	def verDadoAtualLocal(self) -> int:
		pass

	def verColunaAtualLocal(self) -> int:
		pass

	def verificarDadoIgualNoOponente(self, dadoAtual : int, colunaAtual : int) -> bool:
		pass

	def destruirDadoOponente(self, dadoAtual : int, colunaAtual : int):
		pass

	def pegarDadosColunaOponente(self, colunaAtual : int) -> list: #list com 3 ints
		pass

	def verDadoAtualRemoto(self) -> int:
		pass

	def verColunaAtualRemoto(self) -> int:
		pass

	def verificarDadoIgualNoLocal(self, dadoAtual : int, colunaAtual : int) -> bool:
		pass

	def destruirDadoLocal(self, dadoAtual : int, colunaAtual : int):
		pass

	def pegarPontuacaoColunasLocal(self) -> list: #list com 3 ints
		pass

	def pegarPontuacaoColunasRemoto(self) -> list: #list com 3 ints
		pass

	def pegarPontuacaoTotalLocal(self) -> int:
		pass

	def pegarPontuacaoTotalRemoto(self) -> int:
		pass

	def inverteTurnos(self):
		pass

	def get_partida_andamento(self) -> bool:
		pass

	def pegarDadosColunaLocal(self, colunaAtual : int) -> list: #list com 3 ints
		pass

