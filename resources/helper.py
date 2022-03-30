import matplotlib.pyplot as plt


file = open("info.txt","r+") 


count_verdi=0
count_arancioni=0

lstSpeed=[]
lstMemory=[]

for linea in file.readlines():
	#split riga con divisore |
	parti = linea.split('|')
	colore=parti[3]
	speed=parti[6]
	memory=parti[7]

	#modifica colore che ha la forma ':colore_circle:' in 'colore'
	colore=colore.replace('_circle:','')
	colore=colore.replace(':','')
	colore=colore.strip()

	#modifica speed che ha la forma 'xy.zk %' in 'xy.zk'
	speed=speed.replace('%','')
	speed=speed.strip()

	#modifica memory che ha la forma 'xy.zk %' in 'xy.zk'
	memory=memory.replace('%','')
	memory=memory.strip()


	#aggiorna contatori
	if(colore=='green'):
		count_verdi=count_verdi+1
	if(colore=='orange'):
		count_arancioni=count_arancioni+1

	if not speed=='**too slow!**':
		lstSpeed.append(float(speed))

	if not memory=='**too memory!**':
		lstMemory.append(float(memory))




#grafico a barre
data= [count_verdi,count_arancioni]
label=['green','orange']
color=['#00D26A','##FF6723']
plt.bar(label, data,color=label)
plt.xlabel("DIFFICOLTÀ")
plt.ylabel("No. SFIDE COMPLETATE")
plt.title("SFIDE TOTALI: "+str(count_verdi+count_arancioni))
plt.savefig('bar.png')

plt.clf()


#grafico speed
plt.hist(lstSpeed,10)
plt.title("VELOCITÀ")
plt.xlabel("PIU VELOCE DELL'x%")
plt.ylabel("No. SFIDE COMPLETATE")
plt.savefig('speed.png')

plt.clf()


#grafico memory
plt.hist(lstMemory,10)
plt.title("MEMORIA")
plt.xlabel("MENO MEMORIA DELL'x%")
plt.ylabel("No. SFIDE COMPLETATE")
plt.savefig('memory.png')

plt.clf()
