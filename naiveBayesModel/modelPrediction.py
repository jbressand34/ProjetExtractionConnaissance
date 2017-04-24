"""
	Script de prédiction des affectations de classes par un modèle
	Ce script prend en entrée un modèle et des données prétraités pour la prédiction.
	/!\ les données de prédiction doivent être au même format que les données
	d'entrainement du model
	Ce script ne produit pas d'output , il se contente d'afficher les résultats
"""
import os

print("Liste des modeles :")
os.system("ls models")

#Recupération du nom du fichier contenant le modele
modele = input("Quel modele souhaiter vous utiliser?\n")
modele = "models/"+modele

#Si le fichier du model existe
if os.path.isfile(modele):

	#Récupération du nom du classifieur utilisé dans le modele.
	#Je ne pense pas qu'on puisse récupérer le nom du classifieur autrement
	classifieur = input("Quel est le classifieur de ce model ? Par exemple weka.classifiers.bayes.NaiveBayes\n")

	#Récupération du nom du fichier des données de prédiction
	#/!\ les données de test doivent être au même format que les données
	# d'entrainement du model
	print("Liste des fichiers contenant les données prétraités pour la prédiction :")
	os.system("ls dataForPredictionPreprocessed")
	query = "Quel fichier contenant les données prétraitées pour la prédiction voulez-vous utiliser ?\n"
	query += "/!\\ Les données doivent être au même format que celles utilisées pour entrainer le model\n"
	donneesPredictionPretraitees = input(query)
	donneesPredictionPretraitees = "dataForPredictionPreprocessed/"+ donneesPredictionPretraitees
	#Si le fichier des données de prediction existe
	if os.path.isfile(donneesPredictionPretraitees):
		fichierResultats = input("Quel nom de fichier pour les resultats?\n")
		fichierResultats = "resultsPrediction/"+fichierResultats
		os.system("java "+classifieur+" -l "+modele+" -T "+donneesPredictionPretraitees+" -c 1 -p 0 > "+fichierResultats)
		print("Fichier "+fichierResultats+" créé")
		print("done")
	else :
		print(donneesPredictionPretraitees+" n'est pas un fichier")
else :
	print(modele+" n'est pas un fichier")
