import sys
import os
from os import listdir
import time
import shutil


def RemoveDuplicates(listaDup):
	listaSinDup = list(dict.fromkeys(listaDup))
	return listaSinDup

MainDir = sys.argv[1]

if sys.argv [2] == '--check':
	if os.path.exists(MainDir):
		print('Si existe')
	else:
		print('no existe')


elif os.path.exists(str(MainDir)):
	listOfFiles = [file for file in listdir(MainDir)]
	listOfTypes = []
	print(listOfFiles)

	for archivo in listOfFiles:
		if '.' in archivo: # Si el nombre tiene un punto considero que lo que procede es su extensión.
			if archivo == 'desktop.ini': # El escritorio tiene este archivo que lo inicializa al bootear.
				continue

			auxVar = archivo.split('.')
			listOfTypes.append(auxVar[1])


	listOfTypes = RemoveDuplicates(listOfTypes)

	for tipo in range(len(listOfTypes)):
		NewDir = MainDir + f'/{listOfTypes[tipo]}'
		os.mkdir(NewDir)
	

	for i in range(len(listOfFiles)):
		for z in range(len(listOfTypes)):
			if listOfFiles[i].endswith(listOfTypes[z]):
				shutil.move(MainDir + f'/{listOfFiles[i]}', MainDir + f'/{listOfTypes[z]}')

else:
	print(f'El directorio:  "{MainDir}" no existe')
