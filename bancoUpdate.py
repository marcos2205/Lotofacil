#!/usr/bin/python3
#-*- coding: utf8 -*-

import requests
import json
from pymongo import MongoClient

#modulo criado para carga inicial e atualizacao a cada jogo
def atualizajogo():
	#captura dados da lotofacil 
	resp = requests.get('https://api.vitortec.com/loterias/lotofacil/v1.2/')
	
	#convert tupo request para dicionario com o json
	obj = json.loads(resp.text)
	
	#conect ao MONGODB
	client = MongoClient('127.0.0.1')
	#use na database
	db = client['lotofacil']

	if obj["status"] == True:
		#verifica se o jogo ja existe no banco e altera a variavel grava
		grava = True
		for x in db.jogos.find():
			if x["Concurso"] == obj["data"]["concurso"]:
				grava = False
			else:
				grava = True
		#caso não exista o concurso no banco, será gravado
		if grava == True:
			db.jogos.insert({"Concurso":obj["data"]["concurso"],
				"Data":obj["data"]["data"],
				 "RealizadoLocal":obj["data"]["realizacao"]["local"],
				 "RealizadoCidade":obj["data"]["realizacao"]["cidade"],
				 "RealizadoEstado":obj["data"]["realizacao"]["uf"],
				 "Numeros":obj["data"]["resultado"]["ordemSorteio"],
				 "Ganhadores15":obj["data"]["ganhadores"]["15Acertos"]\
				 ["quantidade"],
				 "Premio15":obj["data"]["ganhadores"]["15Acertos"]["valor"],
				 "Ganhadores14":obj["data"]["ganhadores"]["14Acertos"]\
				 ["quantidade"],
				 "Premio14":obj["data"]["ganhadores"]["14Acertos"]["valor"],
				 "Ganhadores13":obj["data"]["ganhadores"]["13Acertos"]\
				 ["quantidade"],
				 "Premio13":obj["data"]["ganhadores"]["13Acertos"]["valor"],
				 "Ganhadores12":obj["data"]["ganhadores"]["12Acertos"]\
				 ["quantidade"],
				 "Premio12":obj["data"]["ganhadores"]["12Acertos"]["valor"],
				 "Ganhadores11":obj["data"]["ganhadores"]["11Acertos"]\
				 ["quantidade"],
				 "Premio11":obj["data"]["ganhadores"]["11Acertos"]["valor"],
				 "ProximoConcursoData":obj["data"]["proximoConcurso"]["data"],
				 "ProximoConcursoEstimativa":obj["data"]["proximoConcurso"]\
				 ["estimativa"]
				 })
			print ("gravado", obj["data"]["concurso"])
		else:
			print ("Banco Atualizado")
	else:
		print ("api fora")





	'''
		#carga inicial - leitura do txt com todos os jogos
		x = 0
		with open('concursos.txt', 'r') as f:
			for linha in f.readlines():
				dic = json.loads(linha)
				db.jogos.insert(dic)
				x += 1
				print (x)
	'''