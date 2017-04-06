source = open("dataset3.txt","r")
destination = open("lemmesLignes.txt", "wt")
output = ""

for ligne in source:
	mot = ligne.split("\t")[1]
	token = mot.split("\n")[0]
	token2 = token.split("\r")[0]
	if token2=="ENDOFLINE":
		destination.write(output+"\n")
		output = ""
                token2 = ""
        elif ligne.split("\t")[0]=="NN" or ligne.split("\t")[0]=="JJ" or  ligne.split("\t")[0][:2]=="VV":               
       	        output = output + " "+ token2
	
        
source.close()
destination.close()
