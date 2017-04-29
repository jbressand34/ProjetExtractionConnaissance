#Fichier tree-tagger: cat dataset.txt | tree-tagger-english > lemmesNew.txt

source = open("../naiveBayesModel/dataForTraining/treeTagDatasetEOL.txt","r")
destination = open("lemmesLignes.txt", "wt")
output = ""
compteur = 0

for ligne in source :
	motInit = ligne.split("\t")[0]
	if len(ligne.split("\t")) >2:
		tag = ligne.split("\t")[1]
		lemme = ligne.split("\t")[2].split("\n")[0]
	#print motInit + " " + tag + " "+ lemme
	if "ENDOFLINE" not in ligne:
		if lemme!="<unknown>":
			if output != "":
				if tag =="CD":
					lemme = motInit
					output = output + " " + lemme
				else:
					output = output + " " + lemme	
				#print output
				

			else :
				output = lemme
				#print output
		else:
			print ("mot: " + motInit)
			
			lemme = motInit
			print ("mot: " + lemme)
			output = output + " " + lemme
	else:
		destination.write(output+"\n")
		output = ""
	"""
	token = mot.split("\n")[0]
	token2 = token.split("\r")[0]
	if token2=="ENDOFLINE":
		destination.write(output+"\n")
		output = ""
                token2 = ""
        elif ligne.split("\t")[0]=="NN" or ligne.split("\t")[0]=="JJ" or  ligne.split("\t")[0][:2]=="VV":               
       	        output = output + " "+ token2
	"""
        
source.close()
destination.close()
