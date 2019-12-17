import subprocess
import os
list=["rsa","aes128", "des3"]
list1=["1024","2048","4096"]
list2=[]
suma=0.0
pomc = ""
pomc1 =""
passwd =  os.getenv('Dupa', '')
for i in range(3): 
	for j in range(3):
		for k in range(100):
			temp= subprocess.Popen(['time','openssl','genrsa','-'+list[i],'-passout','pass:dupa','-out','pliki_klucze/'+list[i]+list1[j]+'.txt',list1[j]],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
			stdout,stderr = temp.communicate()
			#print stdout
			for line in stdout.splitlines():
				#lineres = libLAPFF.parseLine(line)
				if line[len(line)-1] == 'k':
					for z in range(len(line)):
						if  (z<4):
							pomc+=line[z]
						if z>8 and z<13:
							pomc1+=line[z]
						if z ==  13:
							break
				
			suma+=float(pomc)
			suma+=float(pomc1)
			print pomc+' '+pomc1+' '+list[i]+' '+list1[j]+' '+str(k)
			pomc = ""
			pomc1 = ""
		suma=suma/100
		list2.append(suma)
print list2
