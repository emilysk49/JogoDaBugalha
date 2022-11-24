#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Coluna(object):
	def __init__(self):
		self._pontuacao : int = None
		self._dados : list = [-1,-1,-1]
	
	def quantidadeDados(self) -> int:
		pass

	def dadosCombinados(self) -> None:
		pass

	def multiplicarDados(self, quantidadeDados : int, valorDado : int) -> int:
		pass

	def haOutroDado(self) -> bool:
		pass

	def soma(self, pontuacao : int, dado : int) -> int:
		pass

	def temVaga(self) -> bool:
		return self._dados[-1] == -1

	def registraDadoColunaSelecionada(self, dadoAtual : int):
		pass

	def removeDado(self, pos : int):
		self._dados[pos] = -1

	def zerarPontuacao(self):
		self._pontuacao = 0

	def getPontuacao(self) -> int:
		return self._pontuacao

	def destruirDado(self, dadoAtual : int):
		pass

	def organizarColuna(self):
		pass

	def pegarDadosColuna(self) -> list: #list de 3 ints
		pass

	def verificarDadoIgual(self, dadoAtual : int) -> bool:
		pass

	

