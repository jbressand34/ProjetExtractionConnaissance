
"""
	Script de construction d'un modèle et d'entrainement
	de ce modèle à partir des données prétraités.
	Ce script prend en entrée un fichier arff (dont le nom
	est demandé au cours le l'exécution à l'utilisateur)
	contenant des données prétraités et dont le premier attribut est la classe.
	Il produit en sortie une sauvegarde du model (le nom du fichier
	est demandé lors de l'exécution à l'utilisateur) et il affiche sur
	le terminal le résultat des tests de cross-validation avec n=10
	n étant le nombre de subdivision du dataset
"""
import os,re

print("Fichiers de données :\n")
os.system("ls ../naiveBayesModel/dataForTrainingPreprocessed")
#Quel fichier de données prétraitées utiliser pour l'entrainement
nomFichier = input("Choisissez le fichier de sortie des pretraitements:\n")
print("\n")


nomFichier = "../naiveBayesModel/dataForTrainingPreprocessed/"+nomFichier

#On verifie que le fichier existe bien
if os.path.isfile(nomFichier):

	#Quel nom donner à la sauvegarde du modele ?
	nomModel = input("Quel nom de fichier voulez-vous donner au model ? (de la forme [a-zA-Z0-9_-]+\.model)\n")
	classifieur = input("Quel classifieur voulez-vous utiliser pour votre modele ? \n Par exemple:\n weka.classifiers.bayes.NaiveBayes,\n weka.classifiers.functions.SMO,\n weka.classifiers.trees.J48,\n weka.classifiers.lazy.IBk \n")
	#classifieur = input("Quel est le classifieur de ce model ? Par exemple weka.classifiers.bayes.NaiveBayes\n")
	
	#Si l nom termine par .model
	if re.match(r"[a-zA-Z0-9_-]+\.model", nomModel):
		nomModel = "../naiveBayesModel/models/"+nomModel
		#creation entrainement et sauvegarde du modele et affichage des résultats de cross-validation
		os.system("java "+classifieur+" -t "+nomFichier+" -x 10 -c first -d "+nomModel)
		print("Fichier "+nomModel+" créé\n")
		print("done\n")
	else:
		print("Le nom du modele "+nomModel+"ne correspond pas à l'expression reguliere")
else:
	print("Le fichier "+nomFichier+" n'existe pas")
