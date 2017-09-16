#!/usr/bin/python3
#-*- coding: utf8 -*-

from bancoUpdate import bancoUpdate
from pymongo import MongoClient

class confereJogo():
	qtdnum = 0
	lista = []

	#conect ao MONGODB
	client = MongoClient('127.0.0.1')
	#use na database
	db = client['lotofacil']

	def __init__(self):
		upd = bancoUpdate()
		upd.atualizajogo()
	
	def inserirJogo(self):
		while True:
			self.qtdnum = int(input("Informe quantos numeros tem seu jogo: "))
			if self.qtdnum < 15 or self.qtdnum > 18:
				print ("Seu jogo deve ter no minimo 15 numeros e no maximo 18")
				continue
			else:
				x = 0
				while x < self.qtdnum:
					n = int(input("Digite o numero %s: " %(x+1)))
					if n <= 0 or n > 25:
						print ("Vc digitar numeros do 1 ao 25")
						continue
					elif n in self.lista:
						print ("numero repetido, digite novamente")
						continue
					else:
						self.lista.append(n)
						x +=1
				break
		concveri = str(input("Digite qual concurso vc quer conferir: "))
		
		result = self.db.jogos.find({"Concurso":concveri})
		for r in result:
			print ("Concurso:")
			print (r["Concurso"])
			print ("Numeros Sorteados:")
			print (r["Numeros"])
			
			resultado= []
			
			for l in self.lista:
				for n in r["Numeros"]:
					if l == int(n):
						resultado.append(l)
			print ("Voce acertou ", len(resultado), " Numeros!!")
			print (resultado)






if __name__ == '__main__':
	njogo = confereJogo()
	njogo.inserirJogo()