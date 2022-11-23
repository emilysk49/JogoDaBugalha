#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Jogador
import Tabuleiro
from typing import List

class LadoDeJogo(object):
	def inicializar(self, id : int, nome : str):
		pass

	def temVaga(self, colunaSelecionada : int) -> long:
		pass

	def registraColunaSelecionada(self, colunaSelecionada : int):
		pass

	def registraDadoColunaSelecionada(self):
		pass

	def limparColunas(self):
		pass

	def registraDadoGirado(self, dadoGirado : int):
		pass

	def ladoCheio(self) -> long:
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

	def checarTurno(self) -> long:
		pass

	def verDadoAtual(self) -> int:
		pass

	def verColunaAtual(self) -> int:
		pass

	def destruirDado(self, dadoAtual : int, colunaAtual : int):
		pass

	def pegarDadosColuna(self, colunaAtual : int) -> int_3_:
		pass

	def verificarDadoIgual(self, dadoAtual : int, colunaAtual : int) -> long:
		pass

	def pegarPontuacaoColunas(self) -> int_3_:
		pass

	def inverteTurno(self):
		pass

	def __init__(self):
		self._colunas : Colunas = None
		self._pontos_totais : int = None
		self._dadoAtual : int = None
		self._colunaAtual : int = None
		self._jogador : Jogador = None
		self._fase : str = None
		self._unnamed_Tabuleiro_ : Tabuleiro = None
		self._unnamed_Jogador_ : Jogador = None
		"""# @AssociationMultiplicity 1
		# @AssociationKind Composition"""
		self._unnamed_Coluna_ = []
		"""# @AssociationMultiplicity 3
		# @AssociationKind Composition"""

