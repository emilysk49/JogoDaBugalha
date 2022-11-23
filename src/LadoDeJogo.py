#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Jogador import Jogador
from Coluna import Coluna

class LadoDeJogo(object):
	def inicializar(self, id : int, nome : str):
		pass

	def temVaga(self, colunaSelecionada : int) -> bool:
		pass

	def registraColunaSelecionada(self, colunaSelecionada : int):
		pass

	def registraDadoColunaSelecionada(self):
		pass

	def limparColunas(self):
		pass

	def registraDadoGirado(self, dadoGirado : int):
		pass

	def ladoCheio(self) -> bool:
		pass

	def getPontuacaoTotal(self) -> int:
		pass

	def getIdJogador(self) -> int:
		pass

	def setVitoria(self):
		pass

	def calcularPontuacao(self):
		pass

	def somaTotal(self):
		pass

	def checarTurno(self) -> bool:
		pass

	def verDadoAtual(self) -> int:
		pass

	def verColunaAtual(self) -> int:
		pass

	def destruirDado(self, dadoAtual : int, colunaAtual : int):
		pass

	def pegarDadosColuna(self, colunaAtual : int) -> list: #list com 3 ints
		pass

	def verificarDadoIgual(self, dadoAtual : int, colunaAtual : int) -> bool:
		pass

	def pegarPontuacaoColunas(self) -> list: #list com 3 ints
		pass

	def inverteTurno(self):
		pass

	def __init__(self):
		self._colunas : list = [] #Marco quem mudou, antes era estranho, lembra q tem q por Coluna *3 aqui
		self._pontos_totais : int = None
		self._dadoAtual : int = None
		self._colunaAtual : int = None
		self._jogador : Jogador = None
		self._fase : str = None

