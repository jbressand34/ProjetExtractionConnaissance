"""
	Script de prétraitement des données d'entrainement.
	Ce script prend en entrée les fichiers dataset.txt
	et labels.csv  dans dataForTraining et produit en sortie un dataset 
	dans le répertoire dataForTrainingPreprocessed au format arff
	(le nom du fichier est demandé dynamiquement en input dans le terminal)
	sur lequel on a aplliqué des prétraitements (par exemple StringToWordVector)
	Ce script ce déroule en trois étapes :
	- Combinaison des fichier dataset.txt et labels.csv en un fichier csv
	- Transformation de ce fichier csv en arff
	- Demande à l'utilisateur du nom de l'output et application des filtres weka
	
	Ce script est libre d'utilisation n'hésitez pas à le modifier ;)
"""

import os, re

"""
	Premiere partie :
	Combinaison des fichier dataset.txt et labels.csv en un fichier csv
"""
texte = open("dataForTraining/dataset.txt","r")
labels = open("dataForTraining/labels.csv","r")
combinaison = open("jskthclsitorsyutrtxsly.csv","w")

#Je mets en tête du fichier une ligne contenant le nom des attributs 
combinaison.write("texte,label\n")
t = texte.readline().split("\n")[0]
l = labels.readline()
while t and l:
	#Je dois mettre le texte entre guillement et enlever les virgules du texte
	#car pour transformer en arff, weka veut que le texte soit entre guillemets dans le fichier csv
	#et le fichier csv est mal parsé si il y a des virgules en plein milieu du texte
	combinaison.write("\""+t.replace("\"","'")+"\""+","+l)
	#Je dois aussi enlever le retour a la ligne à la fin du texte, curieusement je n'ai pas ce probleme avec les labels
	t = texte.readline().split("\n")[0]
	l = labels.readline()

texte.close()
labels.close()
combinaison.close()


"""
	Deuxième partie :
	Transformation de ce fichier csv en arff
"""
# L'option -S "i-j" signifie que les ieme jusqu'à jeme attributs sont des strings
# L'option -L "i-j:A,...,Z" signifie que les ieme jusqu'à jeme attributs sont nominals
# c'est à dire prenent des valeurs dans l'ensemble donné {A,...,Z}
os.system("java -Xmx2048M weka.core.converters.CSVLoader jskthclsitorsyutrtxsly.csv -S \"1-1\" -L \"2-2:-1,1\" > jskthclsitorsyutrtxsly.arff")

"""
	Troisième partie :
	Demande à l'utilisateur du nom de l'output et application des filtres weka
"""

nomFichierSortie = input("Quel nom de fichier voulez-vous donner au fichier de sortie en Arff ? (de la forme [a-zA-Z0-9_-]+\.arff)\n")

# Je fais un test avec une expression régulière pour verifier que le nom de fichier termine bien en .arff
if re.match(r"[a-zA-Z0-9_-]+\.arff", nomFichierSortie):
	nomFichierSortie = "dataForTrainingPreprocessed/"+nomFichierSortie
	# J'applique le filtre StringToWordVector à mon fichier temporaire arff en input et j'écris dans le fichier que l'utilisateur m'a spécifié
	os.system("java -Xmx2048M weka.filters.unsupervised.attribute.StringToWordVector -L -i jskthclsitorsyutrtxsly.arff -o "+nomFichierSortie + " -stopwords-handler \"weka.core.stopwords.WordsFromFile -stopwords stopwords.txt\" ")
	print("Fichier "+nomFichierSortie+" créé")
else:
	print("Le nom de fichier "+nomFichierSortie+"ne correspond pas à l'expression reguliere")


# Suppression des fichiers temporaires ...
os.system("rm jskthclsitorsyutrtxsly.csv")
os.system("cp jskthclsitorsyutrtxsly.arff dataForTesting/fichierUtilePourPretraitementDataTest.arff")
print("Fichier dataForTesting/fichierUtilePourPretraitementDataTest.arff créé")
os.system("cp jskthclsitorsyutrtxsly.arff dataForPrediction/fichierUtilePourPretraitementDataPrediction.arff")
print("Fichier dataForPrediction/fichierUtilePourPretraitementDataPrediction.arff créé")
os.system("rm jskthclsitorsyutrtxsly.arff")
print("done")
