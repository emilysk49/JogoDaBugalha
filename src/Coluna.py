#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Coluna(object):
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
		temVaga = False
		for i in range(3):
			if self._dados[i] == -1
				temVaga = True
				break		
		return temVaga

	def registraDadoColunaSelecionada(self, dadoAtual : int):
		for i in range(3):
			if self._dados[i] == -1
				self._dados[i] = dadoAtual
				break
				

	def removeDado(self, pos : int):
		self._dados[pos] = -1

	def zerarPontuacao(self):
		self._pontuacao = 0

	def getPontuacao(self) -> int:
		return self._pontuacao

	def destruirDado(self, dadoAtual : int):
		aux : int
		for i in range(3):
			aux = self._dados[i]
			if aux == dadoAtual:
				self._dados[i] = -1

	def organizarColuna(self):
		for i in range(3):
			for j in range(2):
				if self._dados[j] == -1 and self._dados[j+1] != -1:
					self._dados[j] = self._dados[j+1] 
					self._dados[j+1] = -1

	def pegarDadosColuna(self) -> list: #list de 3 ints
		return self._dados

	def verificarDadoIgual(self, dadoAtual : int) -> bool:
		existem = False
		aux : int
		for i in range(3):
			aux = self.dados[i]
			if aux == dadoAtual:
				existem = True
				break
		return existem

	def __init__(self):
		self._pontuacao : int = None
		self._dados : int = None