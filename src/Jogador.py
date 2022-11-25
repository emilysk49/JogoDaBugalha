#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Jogador(object):
	def __init__(self):
		self._nome : str = ""
		self._vencedor : bool = False
		self._turno : bool = False
		self._id : int = -1
	
	def inicializar(self, id : int, nome : str):
		self._nome = nome
		self._id = id

	def resetJogador(self):
		self._nome = ""
		self._vencedor = False
		self._turno = False
		self._id = 0

	def getId(self) -> int:
		return self._id

	def setVitoria(self):
		self._vencedor = True

	def checarTurno(self) -> bool:
		return self._turno

	def inverteTurno(self):
		self._turno = not self._turno
	


