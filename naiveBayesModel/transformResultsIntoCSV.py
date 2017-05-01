import os

os.system("ls resultsPrediction")
resultsToTransform = input("Quel fichier de resultats voulez-vous transformer en csv ?\n")

resultsToTransform = "resultsPrediction/"+resultsToTransform

if os.path.isfile(resultsToTransform):
	resultInput = open(resultsToTransform, "r")

	os.system("ls dataForPrediction")
	texte = input("Quel fichier contient les instances texte ?\n")

	texte = "dataForPrediction/"+texte

	if os.path.isfile(texte):
		texteInput = open(texte, "r")

		nameOutput = input("Quel nom de fichier csv en sortie ?\n")

		output = open("resultsPredictionCSV/"+nameOutput,"w")

		r = resultInput.readline()

		while len(r.split(":")) < 3:
			r = resultInput.readline()

		for line in texteInput:
			t = line.split("\n")[0].replace(",","")
			result =  r.split(":")[2].split(" ")[0]
			output.write(t+", "+result+"\n")
			r = resultInput.readline()

		output.close()

		texteInput.close()
	else:
		print("Le fichier "+texte+" n'existe pas")

	resultInput.close()
else:
	print("Le fichier "+resultsToTransform+" n'existe pas")