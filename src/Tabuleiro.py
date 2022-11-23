#!/usr/bin/python
# -*- coding: UTF-8 -*-
import LadoDeJogo
from Interface import ActorPlayer
from typing import List

class Tabuleiro(object):
	def iniciarPartida(self, *jogadores : str*, idJogadorLocal : str):
		pass

	def temVaga(self, colunaSelecionada : int) -> long:
		pass

	def registraColunaSelecionada(self, colunaSelecionada : int):
		pass

	def registraDadoColunaSelecionada(self):
		pass

	def reiniciarTabuleiro(self):
		pass

	def registrarDadoGirado(self, dadoGirado : int):
		pass

	def verificarTabuleiroCheio(self) -> long:
		pass

	def quemGanhou(self) -> int:
		pass

	def calcularPontuacao(self):
		pass

	def partidaEmAndamento(self):
		pass

	def fimPartida(self):
		pass

	def checarTurnoLocal(self) -> long:
		pass

	def verDadoAtualLocal(self) -> int:
		pass

	def verColunaAtualLocal(self) -> int:
		pass

	def verificarDadoIgualNoOponente(self, dadoAtual : int, colunaAtual : int) -> long:
		pass

	def destruirDadoOponente(self, dadoAtual : int, colunaAtual : int):
		pass

	def pegarDadosColunaOponente(self, colunaAtual : int) -> int_3_:
		pass

	def verDadoAtualRemoto(self) -> int:
		pass

	def verColunaAtualRemoto(self) -> int:
		pass

	def verificarDadoIgualNoLocal(self, dadoAtual : int, colunaAtual : int) -> long:
		pass

	def destruirDadoLocal(self, dadoAtual : int, colunaAtual : int):
		pass

	def pegarPontuacaoColunasLocal(self) -> int_3_:
		pass

	def pegarPontuacaoColunasRemoto(self) -> int_3_:
		pass

	def pegarPontuacaoTotalLocal(self) -> int:
		pass

	def pegarPontuacaoTotalRemoto(self) -> int:
		pass

	def inverteTurnos(self):
		pass

	def get_partida_andamento(self) -> long:
		pass

	def pegarDadosColunaLocal(self, colunaAtual : int) -> int_3_:
		pass

	def __init__(self):
		self._partida_andamento : long = None
		self._ladoDoJogoLocal : LadoDeJogo = None
		self._ladoDoJogoRemoto : LadoDeJogo = None
		self._unnamed_ActorPlayer_ : ActorPlayer = None
		self._unnamed_LadoDeJogo_ = []
		"""# @AssociationMultiplicity 2
		# @AssociationKind Composition"""

