#!/usr/bin/python3
import docker
import sys
import requests


#Création d'une fonction qui permet de vérifier si une URL existe et que cette URL est une URL github. 
def checkUrl(url):
	request = requests.get(url)
	if request.status_code == 200:
		if "github.com" in url:
			return True;
		else:
			return False;		
	else:
		return False;
	   

print("\tPlease fill in the arguments following the example below")
print("\tExample of valid arguments: python3 composeOperator.py link_github image_name")

# récupération du lien github saisie par l'utilisateur
link_github = sys.argv[1]

'''On vérifie le nombre d'argument et on fait appel à la fonction checkUrl pour vérifier l'URL.
   Si le nombre d'argument vaut 3 et que l'URL est valide alors on crée  le fichier Dockerfile dans lequel
   on édite les instructions qui vont permettre la création d'une image.
'''
if len (sys.argv) ==3 and checkUrl(link_github)==True:
    fichier_Dockerfile = open("Dockerfile", "w")
    fichier_Dockerfile.write(
                    "\nFROM ubuntu:latest"
                    "\nMAINTAINER rosemondetraore <benedicte.rosemonde.traore@gmail.com>\n"
                    "\nENV TZ=Europe/Paris\n"
                    "\nRUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone\n"
                    "\nRUN apt-get update\n"
                    "\nRUN apt-get -y upgrade\n"
                    "\nRUN apt-get install -y git\n"
                    "\nRUN apt-get -y install apache2\n"
                    "\nRUN mkdir /var/www/html/medibed\n"                           
                    "\nRUN git clone "+link_github +" /var/www/html/medibed\n"
                    "\nENV APACHE_RUN_USER www-data\n"
                    "\nENV APACHE_RUN_GROUP www-data\n"
                    "\nENV APACHE_LOG_DIR /var/log/apache2\n"
                    "\nENV APACHE_LOCK_DIR /var/lock/apache2\n"
                    "\nENV APACHE_PID_FILE /var/run/apache2.pid\n"
                    "\nEXPOSE 80\n"
                    "\nCMD /usr/sbin/apache2ctl -D FOREGROUND")
    fichier_Dockerfile.close()
'''
Dans cette partie, on récupère le nom de l'image saisie par l'utilisateur puis on crée l'image
et on affiche la liste la liste des images crées
'''
    nom_image = sys.argv[2]
    client = docker.from_env()
    print("Your image is being created ...")
    client.images.build(path = "./",tag = nom_image)
    print("Your image creation was successful!!!!")
    print("Verification of the creation of your image")
    print(client.images.get(nom_image))
       	  
else:
	print("You have misinformed the arguments")

print("End of program")
