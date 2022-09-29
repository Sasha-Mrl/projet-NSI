chr = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
mot = 0
vie1 = '______|___'

vie2 = '''          |		
	      |	             
	      |		
	      |	           
	      |
   _______|___'''

vie3 = '''   ______________
	     |		
	     |		
	     |	             
	     |		
	     |	             
	     |
   ______|___ '''

vie4 = '''      ______________
	      |		|
	      |		o
	      |	            
	      |		
	      |	             
	      |
    ______|___ '''

vie5 = '''
        ______________
	      |		|
	      |		o
	      |	    |
	      |		|
	      |	             
	      |
    ______|___ '''

vie6 = '''      ______________
	      |		|
	      |		o
	      |	   /|\\
	      |		|
	      |	             
	      |
   _______|___ '''

vie7 = '''______________
	      |		|
	      |		o
	      |	   /|\\
	      |		|
	      |	   / \\
	      |
_____	__|___'''
chr_2 = [vie1, vie2, vie3, vie4, vie5, vie6, vie7,]


while mot == 0:
    mot_secret = str(input("Proposez un mot secret :"))
    for i in range(len(mot_secret)): 
        if mot_secret[i] not in chr:
            print ("Des caractères ne sont pas valides (chiffres interdits)")
        elif mot_secret[i] in chr:
            mot = 1      #sortir de la boucle et entrer dans le jeu.

if mot ==1:
    print ("")  #pour sauter des lignes et faire une console plus propre
    print ("")
    print ("")
    print ("Le mot à trouver est le suivant")
    print ("")
    
affichage = ""
for i in mot_secret:
   affichage = affichage + "_ " #pour afficher le nombre de tiret correspondant au mot
print (affichage)
print ("") 
print ("vous avez 7 vies")
print ("")
V = 7
n = 0  # variable pour l'affichage du pendu
while V > 0 :
    l = str(input("proposez une lettre :"))
    if l in mot_secret:
        print ("")
        print("la lettre est dans le mot.")
        V = V
    else:
        print ("")
        print("la lettre n’est pas dans le mot")
        print ("")
        V = V-1
        print("il vous reste", V , "vie(s)")
        print ("")
        print(chr_2[0+n]) # pour faire apparaitre chaque étape du pendu
        n=n+1 
    if V == 0 :
        print("Vous avez perdu, le mot était", mot_secret)
    for i in range(len(mot_secret)):
        if l in mot_secret[i] :
            print(l,"")
            
        else:
            print("_")
       
    
