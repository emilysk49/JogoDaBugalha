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
		self._colunas[self._colunaAtual].registraDadoColunaSelecionada(self._dadoAtual)

	def limparColunas(self):
		for col in range(0,3):
			for pos in range(0,3):
				self._colunas[col].removeDado(pos)
			self._colunas[col].zerarPontuacao()
		self._fase = "naoPartida"

	def registraDadoGirado(self, dadoGirado : int):
		self._fase = "posicionar"
		self._dadoAtual = dadoGirado

	def ladoCheio(self) -> bool:
		num_dados : int = 0
		for col in range(3):
			num_dados += self._colunas[col].quantidadeDados()
		if num_dados == 9: #cheio
			self._fase = "fim"
			return True
		else: #nao cheio
			self._fase = "espera"
			return False

	def getPontuacaoTotal(self) -> int:
		return self._pontos_totais

	def getIdJogador(self) -> int:
		return self._jogador._id

	def setVitoria(self):
		self._jogador.setVitoria()

	def calcularPontuacao(self):
		for c in self._colunas:
			c.dadosCombinados()
		self.somaTotal()

	def somaTotal(self):
		for c in self._colunas:
			pontos += c.getPontuacao()
		self._pontos_totais = pontos
				

	def checarTurno(self) -> bool:
		return self._jogador.checarTurno()

	def verDadoAtual(self) -> int:
		return self._dadoAtual

	def verColunaAtual(self) -> int:
		return self._colunaAtual

	def destruirDado(self, dadoAtual : int, colunaAtual : int):
		self._colunas[colunaAtual].destruirDado(dadoAtual)
		self._colunas[colunaAtual].organizarColuna()

	def pegarDadosColuna(self, colunaAtual : int) -> list: #list com 3 ints
		return self._colunas[colunaAtual].pegarDadosColuna()

	def verificarDadoIgual(self, dadoAtual : int, colunaAtual : int) -> bool:
		return self._colunas[colunaAtual].verificarDadoIgual(dadoAtual)

	def pegarPontuacaoColunas(self) -> list: #list com 3 ints
		pontosColuna = []
		for col in range(3):
			pontosColuna.append(self._colunas[col].getPontuacao())
		return pontosColuna

	def inverteTurno(self):
		self._jogador.inverteTurno()
		if self._jogador._turno == True:
			self._fase = "lancarDado"

	

