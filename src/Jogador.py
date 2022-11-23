#!/usr/bin/python
# -*- coding: UTF-8 -*-
import LadoDeJogo
from typing import List

class Jogador(object):
	def inicializar(self, id : int, nome : str):
		pass

	def resetJogador(self):
		pass

	def getId(self) -> int:
		return self._id

	def setVitoria(self):
		pass

	def checarTurno(self) -> long:
		pass

	def inverteTurno(self):
		pass

	def __init__(self):
		self._nome : str = None
		self._vencedor : long = None
		self._turno : long = None
		self._dadoAtual : int = None
		self._colunaAtual : int = None
		self._colunas : Colunas* = None
		self._pontuacaoTotal : int = None
		self._id : int = None
		self._unnamed_LadoDeJogo_ : LadoDeJogo = None

