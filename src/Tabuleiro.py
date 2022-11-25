#!/usr/bin/python
# -*- coding: UTF-8 -*-
from LadoDeJogo import LadoDeJogo

class Tabuleiro():
	def __init__(self):
		self._partida_andamento : bool = False
		self._ladoDoJogoLocal : LadoDeJogo = LadoDeJogo()
		self._ladoDoJogoRemoto : LadoDeJogo = LadoDeJogo()


	def iniciarTabuleiro(self, jogadores : list):
		jogadorLocal_nome = jogadores[0][0]
		jogadorLocal_id = jogadores[0][1]
		jogadorLocal_order = jogadores[0][2]
		jogadorRemoto_nome = jogadores[1][0]
		jogadorRemoto_id = jogadores[1][1]
		self._ladoDoJogoLocal.inicializar(jogadorLocal_id, jogadorLocal_nome)
		self._ladoDoJogoRemoto.inicializar(jogadorRemoto_id, jogadorRemoto_nome)

		self.partidaEmAndamento()

		if jogadorLocal_order == "1": #Vez do jogadorLocal
			print("vc comeca")
			self._ladoDoJogoLocal.inverteTurno()
		else:
			print("vc espera")
			self._ladoDoJogoRemoto.inverteTurno()


	def temVaga(self, colunaSelecionada : int) -> bool:
		return self._ladoDoJogoLocal.temVaga(colunaSelecionada)

	def registraColunaSelecionada(self, colunaSelecionada : int):
		self._ladoDoJogoLocal.registraColunaSelecionada(colunaSelecionada)

	def registraDadoColunaSelecionada(self):
		self._ladoDoJogoLocal.registraDadoColunaSelecionada()

	def reiniciarTabuleiro(self):
		self._ladoDoJogoLocal.limparColunas()
		self._ladoDoJogoRemoto.limparColunas()

	def registrarDadoGirado(self, dadoGirado : int):
		self._ladoDoJogoLocal.registraDadoGirado(dadoGirado)

	def verificarTabuleiroCheio(self) -> bool:
		local = self._ladoDoJogoLocal.ladoCheio()
		remoto = self._ladoDoJogoRemoto.ladoCheio()
		return (local or remoto)

	def quemGanhou(self) -> int:
		local = self._ladoDoJogoLocal.getPontuacaoTotal()
		remoto = self._ladoDoJogoRemoto.getPontuacaoTotal()
		self.fimPartida()
		if local > remoto:
			return 0
		elif remoto > local:
			return 1
		else:
			return -1

	def calcularPontuacao(self):
		self._ladoDoJogoLocal.calcularPontuacao()
		self._ladoDoJogoRemoto.calcularPontuacao()

	def partidaEmAndamento(self):
		self._partida_andamento = True

	def fimPartida(self):
		self._partida_andamento = False

	def checarTurnoLocal(self) -> bool:
		return self._ladoDoJogoLocal.checarTurno()

	def verDadoAtualLocal(self) -> int:
		return self._ladoDoJogoLocal.verDadoAtual()

	def verColunaAtualLocal(self) -> int:
		return self._ladoDoJogoLocal.verColunaAtual()

	def verificarDadoIgualNoOponente(self, dadoAtual : int, colunaAtual : int) -> bool:
		return self._ladoDoJogoRemoto.verificarDadoIgual(dadoAtual, colunaAtual)

	def destruirDadoOponente(self, dadoAtual : int, colunaAtual : int):
		self._ladoDoJogoRemoto.destruirDado(dadoAtual, colunaAtual)

	def pegarDadosColunaOponente(self, colunaAtual : int) -> list: #list com 3 ints
		return self._ladoDoJogoRemoto.pegarDadosColuna(colunaAtual)

	def verDadoAtualRemoto(self) -> int:
		return self._ladoDoJogoRemoto.verDadoAtual()

	def verColunaAtualRemoto(self) -> int:
		return self._ladoDoJogoRemoto.verColunaAtual()

	def verificarDadoIgualNoLocal(self, dadoAtual : int, colunaAtual : int) -> bool:
		return self._ladoDoJogoLocal.verDadoAtual(dadoAtual, colunaAtual)

	def destruirDadoLocal(self, dadoAtual : int, colunaAtual : int):
		self._ladoDoJogoLocal.destruirDado(dadoAtual, colunaAtual)

	def pegarPontuacaoColunasLocal(self) -> list: #list com 3 ints
		return self._ladoDoJogoLocal.pegarPontuacaoColunas()

	def pegarPontuacaoColunasRemoto(self) -> list: #list com 3 ints
		return self._ladoDoJogoRemoto.pegarPontuacaoColunas()

	def pegarPontuacaoTotalLocal(self) -> int:
		return self._ladoDoJogoLocal.getPontuacaoTotal()

	def pegarPontuacaoTotalRemoto(self) -> int:
		return self._ladoDoJogoRemoto.getPontuacaoTotal()

	def inverteTurnos(self):
		self._ladoDoJogoLocal.inverteTurno()
		self._ladoDoJogoRemoto.inverteTurno()

	def get_partida_andamento(self) -> bool:
		return self._partida_andamento

	def pegarDadosColunaLocal(self, colunaAtual : int) -> list: #list com 3 ints
		return self._ladoDoJogoLocal.pegarDadosColuna(colunaAtual)
	
	def setVitoriaLocal(self):
		self._ladoDoJogoLocal.setVitoria()

	def setVitoriaRemota(self):
		self._ladoDoJogoRemoto.setVitoria()

