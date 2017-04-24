"""
	Script de test d'un modèle
	Ce script prend en entrée un modèle et des données de test prétraités.
	/!\ les données de test doivent être au même format que les données
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

	#Récupération du nom du fichier de test
	#/!\ les données de test doivent être au même format que les données
	# d'entrainement du model
	print("Fichiers des données de test prétraitées :")
	os.system("ls dataForTestingPreprocessed")
	query = "Quel fichier contenant les données de test prétraitées voulez-vous utiliser ?\n"
	query += "/!\\ Les données doivent être au même format que celles utilisées pour entrainer le model\n"
	donneesTestPretraitees = input(query)
	donneesTestPretraitees = "dataForTestingPreprocessed/"+donneesTestPretraitees

	#Si le fichier des données de test existe
	if os.path.isfile(donneesTestPretraitees):
		#Exécution du test et affichage des résultat
		os.system("java "+classifieur+" -l "+modele+" -T "+donneesTestPretraitees+" -c 1")
	else:
		print(donneesTestPretraitees+" n'est pas un fichier")
else:
	print(modele+" n'est pas un fichier")	
print("done")