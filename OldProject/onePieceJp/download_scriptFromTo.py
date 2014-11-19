from os import system
from os import chdir
from os import listdir
import sys



from os import system
from os import listdir
from os import chdir


def convert2pdf(book_number):
    new_names = [ ('0'*(3-len(number[0]))+number[0]+'.jpg',number[1])  for number in  [(x.split('.')[0],x) for x in listdir('.') if 'error' not in x]]
    for new_name in new_names:
        system("mv "+new_name[1]+" "+new_name[0])
    
    system("convert *.jpg ../book"+book_number+".pdf")
    chdir("..")
    system("rm -r book"+book_number)
    print "book " + book_number + " successfully created"

def error():
    f = open("error")
    x = f.readlines()[-2]
    if "404" in x:
        print "error detected"
        f.close()
        return True
    f.close()
    return False

def fill_number(number,size=3):
    return '0'*(size-len(str(number)))+str(number)

base_url = "http://img2.veryim.com/H/haizeiwang/vol_"
base_url_alternativa = "http://img2.veryim.com/H/haizeiwang/ch_"
base_chapter = ""
base_image = "/"
base_extension = ".jpg"
base_extension_alternativa = ".png"
get_url = lambda x: base_url+base_chapter+str(x[0])+base_image+str(x[1])+base_extension
error_count = 0

def downloadNarutoFromTo(first,last):
    book = first
    while book < last:
        system("mkdir book"+str(book))
        chdir("book"+str(book))
        chapter = 1
        while True:
            print "printing " + "wget("+get_url([book,fill_number(chapter)])+")"
            system("wget "+get_url([book,fill_number(chapter)])+" 2> error")
            if error() == True:
                break
            chapter = chapter + 1

        if chapter == 1:
            system("rm -r book"+str(book))
            break
        convert2pdf(str(book))
        book = book + 1

downloadNarutoFromTo(int(sys.argv[1]),int(sys.argv[2]))
