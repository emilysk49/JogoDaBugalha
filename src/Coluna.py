#!/usr/bin/python
# -*- coding: UTF-8 -*-
import LadoDeJogo
from typing import List

class Coluna(object):
	def quantidadeDados(self) -> int:
		pass

	def dadosCombinados(self) -> None:
		pass

	def multiplicarDados(self, quantidadeDados : int, valorDado : int) -> int:
		pass

	def haOutroDado(self) -> long:
		pass

	def soma(self, pontuacao : int, dado : int) -> int:
		pass

	def temVaga(self) -> long:
		pass

	def registraDadoColunaSelecionada(self, dadoAtual : int):
		pass

	def removeDado(self, pos : int):
		pass

	def zerarPontuacao(self):
		pass

	def getPontuacao(self) -> int:
		return self._pontuacao

	def destruirDado(self, dadoAtual : int):
		pass

	def organizarColuna(self):
		pass

	def pegarDadosColuna(self) -> int_3_:
		pass

	def verificarDadoIgual(self, dadoAtual : int) -> long:
		pass

	def __init__(self):
		self._pontuacao : int = None
		self._dados : int* = None
		self._unnamed_LadoDeJogo_ : LadoDeJogo = None

