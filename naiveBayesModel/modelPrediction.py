"""
	Script de prédiction des affectations de classes par un modèle
	Ce script prend en entrée un modèle et des données prétraités pour la prédiction.
	/!\ les données de prédiction doivent être au même format que les données
	d'entrainement du model
	Ce script ne produit pas d'output , il se contente d'afficher les résultats
"""
import os

print("\nListe des modeles :\n")
os.system("ls ../naiveBayesModel/models")

#Recupération du nom du fichier contenant le modele
modele = input("\nQuel modele souhaiter vous utiliser?\n")
modele = "../naiveBayesModel/models/"+modele

#Si le fichier du model existe
if os.path.isfile(modele):

	#Récupération du nom du classifieur utilisé dans le modele.
	#Je ne pense pas qu'on puisse récupérer le nom du classifieur autrement
	classifieur = input("Quel est le classifieur de ce model ? \nPar exemple \nweka.classifiers.bayes.NaiveBayes\n")

	#Récupération du nom du fichier des données de prédiction
	#/!\ les données de test doivent être au même format que les données
	# d'entrainement du model
	print("\nListe des fichiers contenant les données prétraités pour la prédiction :\n")
	os.system("ls ../naiveBayesModel/dataForPredictionPreprocessed")
	#query = "Quel fichier contenant les données prétraitées pour la prédiction voulez-vous utiliser ?\n"
	#query += "/!\\ Les données doivent être au même format que celles utilisées pour entrainer le model\n"
	donneesPredictionPretraitees = input("Quel fichier contenant les données prétraitées pour la prédiction voulez-vous utiliser ?\n")
	donneesPredictionPretraitees = "../naiveBayesModel/dataForPredictionPreprocessed/"+ donneesPredictionPretraitees
	#Si le fichier des données de prediction existe
	if os.path.isfile(donneesPredictionPretraitees):
		fichierResultats = input("Quel nom de fichier .txt pour les resultats?\n")
		fichierResultats = "../naiveBayesModel/resultsPrediction/"+fichierResultats
		os.system("java "+classifieur+" -l "+modele+" -T "+donneesPredictionPretraitees+" -c 1 -p 0 > "+fichierResultats)
		print("Fichier "+fichierResultats+" créé")
		print("done")
	else :
		print(donneesPredictionPretraitees+" n'est pas un fichier")
else :
	print(modele+" n'est pas un fichier")
