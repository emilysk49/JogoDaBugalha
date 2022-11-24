#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Jogador import Jogador
from Coluna import Coluna

class LadoDeJogo(object):
	def __init__(self):
		self._colunas : list = [] #Marco quem mudou, antes era estranho, lembra q tem q por Coluna *3 aqui
		for i in range(3):
			self._colunas.append(Coluna())
		self._pontos_totais : int = 0
		self._dadoAtual : int = -1
		self._colunaAtual : int = -1
		self._jogador : Jogador = Jogador()
		self._fase : str = "naoPartida"
	
	def inicializar(self, id : int, nome : str):
		self._jogador.resetJogador()
		self._jogador.inicializar(id, nome)
		self._fase = "espera"

	def temVaga(self, colunaSelecionada : int) -> bool:
		if self._colunas[colunaSelecionada].temVaga():
			self._fase = "posicionou"
			return True
		return False

	def registraColunaSelecionada(self, colunaSelecionada : int):
		self._colunaAtual = colunaSelecionada


	def registraDadoColunaSelecionada(self):
		self._colunas[self._colunaAtual][-1] = self._dadoAtual

	def limparColunas(self):
		for col in range(0,3):
			for pos in range(0,3):
				self._colunas[col].removeDado(pos)
			self._colunas[col].zerarPontuacao()

	def registraDadoGirado(self, dadoGirado : int):
		self._fase = "posicionar"
		self._dadoAtual = dadoGirado

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
		self._jogador.inverteTurno()
		if self._jogador._turno == True:
			self._fase = "lancarDado"

	

