import subprocess 
import os
import  getpass
cmd = "time date"
passwd="Dupa"
wielkosc = "1024"
temp = subprocess.Popen(['time','openssl','rsa','-in','pliki_klucze/des34096.txt','-passin','pass:dupa','-out','1000KB.txt'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
stdout,stderr = temp.communicate()



print "dupaaa"
print(stdout)
print (stdout)

