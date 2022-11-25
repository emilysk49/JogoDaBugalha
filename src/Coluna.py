#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Coluna(object):
	def __init__(self):
		self._pontuacao : int = 0
		self._dados : list = [-1,-1,-1]
	
	def quantidadeDados(self) -> int:
		quantidade : int = 0
		for i in self._dados:
			if i != -1:
				quantidade += 1
		return quantidade

	def dadosCombinados(self) -> None:
		self._pontuacao = 0
		tem : bool = False
		jaContou : bool = False
		for i in range(2):
			quantidade = self._dados.count(self._dados[i])
			if (quantidade > 1) and (self._dados[i] != -1):
				num = self._dados[i]
				tem = True
				break

		for c in range(3):
			if self._dados[c] != -1:
				if tem:
					if self._dados[c] == num:
						if not jaContou:
							self._pontuacao += num*quantidade*quantidade
							jaContou = True
					else:	#self._dados[c] != num
						self._pontuacao += self._dados[c]
				else:	#NOT tem
					self._pontuacao += self._dados[c]


	def multiplicarDados(self, quantidadeDados : int, valorDado : int) -> int:
		pass

	def haOutroDado(self) -> bool:
		pass

	def soma(self, pontuacao : int, dado : int) -> int:
		pass

	def temVaga(self) -> bool:
		return self._dados[-1] == -1

	def registraDadoColunaSelecionada(self, dadoAtual : int):
		for i in range(3):
			if self._dados[i] == -1:
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
				if (self._dados[j] == -1) and (self._dados[j+1] != -1):
					self._dados[j] = self._dados[j+1] 
					self._dados[j+1] = -1

	def pegarDadosColuna(self) -> list: #list de 3 ints
		return self._dados

	def verificarDadoIgual(self, dadoAtual : int) -> bool:
		aux : int
		existem : bool = False
		for i in range(0,3):
			aux = self._dados[i]
			if aux == dadoAtual:
				existem = True
				break
		return existem
	

