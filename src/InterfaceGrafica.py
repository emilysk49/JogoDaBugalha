#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Interface import Tk
from Interface import Frame
from Interface import PhotoImage
from Interface import Label
from Interface import ActorPlayer
from Interface import Menu
from typing import List

class InterfaceGrafica(object):
	def desabilitaColunas(self):
		pass

	def notificar(self, mensagem : String):
		pass

	def desabilitaGirarDado(self):
		pass

	def mostrarDadoGirado(self, dadoGirado : int, ehDadoLocal : long):
		pass

	def habilitarColunas(self):
		pass

	def redesenharColunaOponente(self, *dadosAAtualizar : int*, colunaAtual : int):
		pass

	def inserirDadoLocal(self, dadoAtual : int, colunaAtual : int):
		pass

	def atualizarPontos(self, pontuacaoColunasLocal : int_3_, pontuacaoTotalLocal : int, pontuacaoColunasRemoto : int_3_, pontuacaoTotalRemoto : int):
		pass

	def habilitarGirarDado(self):
		pass

	def __init__(self):
		self._main_window : Tk = None
		self._dado_frame : Frame = None
		self._empty : PhotoImage = None
		self._dado1 : PhotoImage = None
		self._dado2 : PhotoImage = None
		self._dado3 : PhotoImage = None
		self._dado4 : PhotoImage = None
		self._dado5 : PhotoImage = None
		self._dado6 : PhotoImage = None
		self._board_view : Label* = None
		self._label_dado1 : Label = None
		self._label_dado2 : Label = None
		self._actorPlayer : ActorPlayer = None
		self._unnamed_ActorPlayer_ : ActorPlayer = None
		self._unnamed_Tk_ : Tk = None
		"""# @AssociationKind Aggregation"""
		self._unnamed_PhotoImage_ = []
		"""# @AssociationMultiplicity 8
		# @AssociationKind Aggregation"""
		self._unnamed_Label_ = []
		"""# @AssociationMultiplicity 26
		# @AssociationKind Aggregation"""
		self._unnamed_Menu_ : Menu = None
		"""# @AssociationKind Aggregation"""
		self._unnamed_Frame_ = []
		"""# @AssociationMultiplicity 2
		# @AssociationKind Aggregation"""
		self._unnamed_ActorPlayer_2 : ActorPlayer = None
		self._unnamed_ActorPlayer_3 : ActorPlayer = None

	def redesenharColunaLocal(self, dadosAAtualizar : int_3_, colunaAtual : int):
		pass

	def inserirDadoOponente(self, dadoAtual : int, colunaAtual : int):
		pass

	def carregaInterface(self):
		pass

