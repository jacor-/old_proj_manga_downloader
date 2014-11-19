from os import system
import sys

def getManga(numero):
    system("mkdir cosa")
    system("wget http://kissmanga.com/Manga/Pokemon-Adventures/"+str(numero)+" -O cosa/check")
    f = open("cosa/check")
    s = f.readlines()
    f.close()
    imgs = [x.split("\"")[1] for x in s if "lstImages.push" in x]
    c = 0
    names = ""
    for img in imgs:
        system("wget "+img + " -O " + 'cosa/'+'0'*(3-len(str(c)))+str(c)+".jpg")
        c = c +1 
    system("cd cosa; convert *.jpg ../book"+str(numero)+".pdf; cd ..;rm -r cosa")
    #system("pdftk "+ names + " cat output book"+str(numero))

for x in range(int(sys.argv[1]), int(sys.argv[2])+1):
    getManga(x)

    
