"""
	Script de prétraitement du fichier contenant les nouvelles données
	texte sur lesquelles faire de la prédiction
	Ce script prend en entrée un fichier texte ou chaque ligne représente une phrase.
	Ce script produit en sortie un fichier arff correspondant (où l'attribut label est ? car inconnu)
	avec les données prétraités (pour faire StringToWordVector, ce script a besoin du fichier arff
	contenant les données d'entrainement avant StringToWordVector, cad le fichier arff avec deux attributs :
	texte et label, car on en a besoin pour appiquer StringToWordVector en mode batch -> voir docs_et_liens_utiles/liens_utiles.txt)

	Ce script se déroule en plusieurs étapes : 
	- On demande à l'utilisateur quel fichier texte doit-on prétraité afin de faire de la prédiction dessus 
	- On créé un fichier csv temporaire à partir du fichier texte contenant deux colonnes : texte et label, la colonne label est remplie de '?'
	- On transforme le fichier csv en un fichier arff avec les deux attributs : texte et label
	- On applique les filtres de weka sur le fichier arff (par exemple StringToWordVector en mode batch -> voir docs_et_liens_utiles/liens_utiles.txt)
"""  
import os,re

print("Fichiers texte pour la prédiction :")
os.system("ls dataForPrediction | egrep \"*\.txt\"")

# On demande à l'utilisateur quel fichier texte doit-on prétraité afin de faire de la prédiction dessus
texte = input("Quel fichier contient les données texte qu'il faut prétraiter ?\n")

texte = "dataForPrediction/"+texte

# Si le fichier texte existe
if os.path.isfile(texte):
	texte=open(texte,'r')
	
	#On créé un fichier csv temporaire à partir du fichier texte contenant deux colonnes : texte et label, 
	#la colonne label est remplie de '?' car les valeurs sont inconnus
	csv = open("skjchgjkbgsmyfbcg.csv",'w')
	csv.write("texte,label\n")
	for t in texte:
		#Je dois mettre le texte entre guillement et enlever les virgules du texte
		#car pour transformer en arff, weka veut que le texte soit entre guillemets dans le fichier csv
		#et le fichier csv est mal parsé si il y a des virgules en plein milieu du texte
		csv.write("\""+t.split("\n")[0].replace(",","").replace("\"","")+"\",?\n")
	print("done csv")
	texte.close()
	csv.close()

	#On transforme le fichier csv en un fichier arff temporaire avec les deux attributs : texte et label
	# L'option -S "i-j" signifie que les ieme jusqu'à jeme attributs sont des strings
	# L'option -L "i-j:A,...,Z" signifie que les ieme jusqu'à jeme attributs sont nominals
	# c'est à dire prenent des valeurs dans l'ensemble donné {A,...,Z}
	os.system("java weka.core.converters.CSVLoader skjchgjkbgsmyfbcg.csv -S \"1-1\" -L \"2-2:-1,1\" > skjchgjkbgsmyfbcg.arff")


	nomFichierSortie = input("Quel nom de fichier voulez-vous donner au fichier de sortie en Arff ? (de la forme [a-zA-Z0-9_-]+\.arff)\n")

	# Je fais un test avec une expression régulière pour verifier que le nom de fichier termine bien en .arff
	if re.match(r"[a-zA-Z0-9_-]+\.arff", nomFichierSortie):
		nomFichierSortie = "dataForPredictionPreprocessed/"+nomFichierSortie
		#On applique les filtres de weka sur le fichier arff (par exemple StringToWordVector en mode batch -> voir docs_et_liens_utiles/liens_utiles.txt)
		# -b : mode batch
		# -i <donnéesEntrainementInput> -o <donnéesEntrainementOutput> : Apllique StringToWordVector normalement
		# -r <donnéesPrédictionInput> -s <donnéesPrédictionOutput> : Applique StringToWordVector en utilisant les attributs générés lors
		#	de la précédente exécution avec -i <input> -o <output>
		os.system("java -Xmx2048M weka.filters.unsupervised.attribute.StringToWordVector -L -b -i dataForPrediction/fichierUtilePourPretraitementDataPrediction.arff -o taoctraotrtoazxio.arff -r skjchgjkbgsmyfbcg.arff -s "+nomFichierSortie+" -stopwords-handler \"weka.core.stopwords.WordsFromFile -stopwords stopwords.txt\" ")
		print("Fichier "+nomFichierSortie+" créé")
		print("done")
	else:
		print("Le nom de fichier "+nomFichierSortie+"ne correspond pas à l'expression reguliere")
	

	# Supression fichiers temporaires
	os.system("rm skjchgjkbgsmyfbcg.csv")
	os.system("rm skjchgjkbgsmyfbcg.arff")
	os.system("rm taoctraotrtoazxio.arff")

else:
	print(texte+" n'est pas un fichier.")