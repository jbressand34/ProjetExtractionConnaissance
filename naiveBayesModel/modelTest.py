"""
	Script de test d'un modèle
	Ce script prend en entrée un modèle et des données de test prétraités.
	/!\ les données de test doivent être au même format que les données
	d'entrainement du model
	Ce script ne produit pas d'output , il se contente d'afficher les résultats
"""
import os

print("Liste des modeles :\n")
os.system("ls ../naiveBayesModel/models")
#Recupération du nom du fichier contenant le modele
modele = input("\nQuel modele souhaiter vous utiliser?\n")
modele = "../naiveBayesModel/models/"+modele

#Si le fichier du model existe
if os.path.isfile(modele):

	#Récupération du nom du classifieur utilisé dans le modele.
	#Je ne pense pas qu'on puisse récupérer le nom du classifieur autrement
	classifieur = input("Quel est le classifieur de ce model ?\n Par exemple\n weka.classifiers.bayes.NaiveBayes\n")

	#Récupération du nom du fichier de test
	#/!\ les données de test doivent être au même format que les données
	# d'entrainement du model
	print("\n")
	os.system("ls ../naiveBayesModel/dataForTestingPreprocessed")
	print("\n")
	
	#query += "/!\\ Les données doivent être au même format que celles utilisées pour entrainer le model\n"
	donneesTestPretraitees = input("Choisissez le fichier de test prétraité ( en .arff): \n")
	os.system("ls ../naiveBayesModel/dataForTestingPreprocessed")
	donneesTestPretraitees = "../naiveBayesModel/dataForTestingPreprocessed/"+donneesTestPretraitees

	#Si le fichier des données de test existe
	if os.path.isfile(donneesTestPretraitees):
		#Exécution du test et affichage des résultat
		os.system("java "+classifieur+" -l "+modele+" -T "+donneesTestPretraitees+" -c 1")
	else:
		print(donneesTestPretraitees+" n'est pas un fichier")
else:
	print(modele+" n'est pas un fichier")	
print("done")