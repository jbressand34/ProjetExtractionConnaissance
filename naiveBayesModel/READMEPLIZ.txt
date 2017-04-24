""""""""""""""""""""""""""""""""""""""""""""""""
		SCRIPTS PYTHON UTILISANT WEKA !!!
		pour ceux qui n'aiment pas java
		et les interfaces graphiques
""""""""""""""""""""""""""""""""""""""""""""""""
Date : 24/04/17

""""""
PLAN :
	0. Prérequis d'utilisation
	1. But de ces scripts
	2. Cas d'utilisation :
		2.1 Construction d'un modèle à partir de données d'entrainement
		2.2 Test d'un modèle sur des données de test
		2.3 Prédictions d'un modèle sur des textes
	3. Remarques
""""""

"""""
0. Prérequis d'utilisation :
	

	Pour utiliser ces scripts vous devez auparavant avoir :
	- Linux
	- Python3 installé.
	- Téléchargé et dézippé l'archive weka-3-8-1.zip stable version
	- Mis le chemin vers weka.jar dans la variable systeme CLASSPATH
		A la fin de votre fichier .bashrc, ajouter la ligne :
			export CLASSPATH=<chemin vers weka.jar>
		par exemple :
			export CLASSPATH=/home/ymerej/weka/weka-3-8-1/weka.jar

		ou si la variable systeme CLASSPATH est déjà définie :
			export CLASSPATH=$CLASSPATH:<chemin vers weka.jar>

		Vous pouvez tester le bon fonctionnement de weka en tapant la commande :
		java weka.classifiers.bayes.NaiveBayes -h

	Ma configuration de pc :
	- Xubuntu 14.04 64bits
	- java version "1.7.0_121"
	- OpenJDK Runtime Environment (IcedTea 2.6.8) (7u121-2.6.8-1ubuntu0.14.04.3)
	- OpenJDK 64-Bit Server VM (build 24.121-b00, mixed mode)

""""

""""
1. But de ces scripts

	
	Ces scripts existent pour le projet d'extraction de connaissance en master 1 DECOL à l'université de Montpellier 2016/2017.
	Le but de ce projet est de faire de la prédiction d'opinion sur un ensemble de textes en utilisant les outils de la plateforme weka : http://www.cs.waikato.ac.nz/ml/weka/
""""

""""
2. Cas d'utiliation :

	"""""""""""""
	2.1 Construction d'un modèle à partir de données d'entrainement

		Pour faire fonctionner les scripts, les données d'entrainement doivent se trouver dans le répertoire dataForTraining.

		Les données d'entrainements consistent en deux fichiers :
		- Un fichier dataset.txt dans lequel chaque ligne correspond à une phrase en anglais
		- Un fichier labels.csv contenant une seule colonne et dans lequel chaque cellule est soit -1 soit 1.
		Ces deux fichiers doivent avoir le même nombre de lignes

		La construction d'un modèle à partir de ces données se déroule en deux grandes étapes :

		- Prétraitement des données d'entrainement

			Pour prétraiter les données d'entrainenment il faut exécuter avec python3 le programme pretraitementDonnesEntrainenement.py

			Lors de l'exécution de ce programme, l'interface du terminal vous demandera d'entrer un nom de fichier se terminant en .arff dans lequel il va sauvegarder les données prétraités. Ce fichier sera dans le répertoire dataForTrainingPreprocessed

			Le programme va aussi créer deux autres fichiers : dataForTesting/fichierUtilePourPretraitementDataset.arff
			et dataForPrediction/fichierUtilePourPretraitementDataPrediction.arff qui ne nous intéressent pas outre mesure.

			FIN

		- Construction du modèle à partir des données prétraités

			Pour construire un modèle à partir des données d'entrainement prétraitées il faut exécuter avec python3 le programme constructionModel.py

			Lors de l'exécution de ce programme, l'interface du terminal va vous demander deux choses : tout d'abord le nom du fichier dans lequel se trouve les données d'entrainement prétraités (le nom du fichier que vous avez choisi à l'étape précédente) et le nom du fichier dans lequel il va sauvegarder le modèle. Ce fichier sera dans le répertoire modèle.

			Le programme va entrainer le modèle sur les données d'entrainement prétraités et vous affichera les résultas de cross-validation avec une division du dataset en 10 sous-ensemble.

			FIN

		FIN

	"""""""""""""

	"""""""""""""
	2.2 Test d'un modèle sur des données de test

		Pour faire fonctionner les scripts, les données de test doivent se trouver dans le répertoire dataForTesting.

		Les données de test doivent être de même nature que les données d'entrainement cad deux fichiers dataset.txt et labels.csv avec respectivement du texte et des -1 ou 1.

		Vous devez avoir créé préalablement un modèle et le fichier :
		 dataForTesting/fichierUtilePourPretraitementDataTest.arff
		qui a du être créé lors de l'exécution du script pretraitementDonneesEntrainement.py.

		Le test d'un modèle existant sur des données de test se déroule en deux étapes :

		- Prétraitement des données de test
			Pour prétraiter les données de test il faut exécuter avec python3 le programme pretraitementDonnesTest.py

			Lors de l'exécution de ce programme, l'interface du terminal vous demandera d'entrer un nom de fichier se terminant en .arff dans lequel il va sauvegarder les données prétraités. Ce fichier sera dans le répertoire dataForTestingPreprocessed

			FIN

		- Test du modèle sur les données de test
			Pour tester le modèle sur les données de test il faut exécuter vec python3 le programme modelTest.py

			Lors de l'exécution de ce programme l'interface du terminal vous demandera d'entrer le nom du fichier dans lequel se trouve le modèle, d'entrer le nom du classifieur qui est utilisé par le modèle (par exemple weka.classifiers.bayes.NaiveBayes) et d'entrer le nom du fichier dans lequel se trouve les données de test prétraités.

			Le programme affichera ensuite dans le terminal les résultats du test.

			FIN
		FIN 

	"""""""""""""


	"""""""""""""
	2.3 Prédictions d'un modèle sur des textes

	Pour faire fonctionner les scripts le fichier contenant les textes sur lesquels va se faire la prédiction doit se trouver dans le répertoire dataForPrediction

	Le fichier contenant les textes pour la prédiction doit avoir un nom se terminant en .txt et chaque ligne de ce fichier est un texte correspondant à une opinion.

	Le modèle doit exister dans un fichier dans le répertoire models et le fichier suivant qui a été cré lors du prétraitement sur les données d'entraineent doit exister :
		dataForPrediction/fichierUtilePourPretraitementDataPrediction.arff

	La prédiction des opinions des textes en utilisant un modèle se déroule en deux étapes.

	- Prétraitement des données de prédiction

		Pour prétraiter les données contenant les textes pour la prédiction on doit exécuter avec python3 le programme pretraitementDonneesPrediction.py

		Lors de l'exécution du programme, l'interface du terminal va vous demander le nom du fichier contenant les textes sur lesquels va se faire la prédiction et le nom du fichier se terminant en .arff qui va contenir les données prétraitées et qui va se trouver dans le répertoire dataForPredictionPreprocessed.

		FIN

	- Application du modèle sur les données prétraité et sauvegarde des résultats

		Pour appliquer le modèle sur les données prétraitées (pour qu'il fasse de la prédiction sur ces données) on doit exécuter avec python3 le programme modelPrediction.py.

		Lors de l'exécution de ce programme, l'interface du terminal va vous demander le nom du fichier contenant le modèle, le nom du classifieur utilisé par ce modèle (par exemple weka.classifiers.bayes.naiveBayes), le nom du fichier contenant les données pour la prédiction prétraitées et enfin le nom du fichier dans lequel il va sauvegarder les résultats de la prédiction.
		Ce fichier sera suvegardé dans le dossier resultsPrediction.

		FIN
	FIN


	"""""""""""""

	FIN

""""


""""
3. Remarques :
	
	- J'ai conçu ces scripts en utilisant weka en ligne de commande. J'ai trouvé de la bonne documentation (partie 1 dans docs_et_liens_utiles/WekaManual-3-8-0.pdf)

	- Pour mes coéquipiers  je propose qu'on créé un repertoire par modèle à la racine du git. Ce scripts se situent dans un dossier à la racine du git nommé naivesBayesModels. Si vous voulez faire des arbres de décision ou du SVM  ou ajouter du TreeTagger en modifiant mon code je propose que vous copiez collez le répertoire naiveBayesModels et que vous travaillez sur cette copie en laissant l'original intact.  

	- J'ai pas mal commenté ça devrait pas poser de problème pour comprendre le code sauf que j'ai utilisé un truc bizarre : le mode batch en StringToWordVector pour les prétaitements pour la prédiction et les tests. J'ai essayé d'expliquer pourquoi et j'ai mis un lien dans le fichier docs_et_liens_utiles/liens_utiles.txt

	- Enjoy

""""