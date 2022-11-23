#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Jogador(object):
	def inicializar(self, id : int, nome : str):
		pass

	def resetJogador(self):
		pass

	def getId(self) -> int:
		return self._id

	def setVitoria(self):
		pass

	def checarTurno(self) -> bool:
		pass

	def inverteTurno(self):
		pass

	def __init__(self):
		self._nome : str = None
		self._vencedor : bool = False
		self._turno : bool = None
		self._id : int = None


