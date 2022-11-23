#!/usr/bin/python
# -*- coding: UTF-8 -*-
from LadoDeJogo import LadoDeJogo

class Tabuleiro(object):
	def iniciarPartida(self, jogadores : str, idJogadorLocal : str):
		pass

	def temVaga(self, colunaSelecionada : int) -> bool:
		pass

	def registraColunaSelecionada(self, colunaSelecionada : int):
		pass

	def registraDadoColunaSelecionada(self):
		pass

	def reiniciarTabuleiro(self):
		pass

	def registrarDadoGirado(self, dadoGirado : int):
		pass

	def verificarTabuleiroCheio(self) -> bool:
		pass

	def quemGanhou(self) -> int:
		pass

	def calcularPontuacao(self):
		pass

	def partidaEmAndamento(self):
		pass

	def fimPartida(self):
		pass

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

	def __init__(self):
		self._partida_andamento : bool = None
		self._ladoDoJogoLocal : LadoDeJogo = None
		self._ladoDoJogoRemoto : LadoDeJogo = None
