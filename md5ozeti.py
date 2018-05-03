import hashlib 
import random
sayac = -1
y = []
n = input("n sayisini giriniz:")
n = int(n)
#dosyaya rastgele rakamlar atılıyor
myFile = open("numbers.txt","w")

for i in range(0, n):
	temp = random.randint(1,9)
	myFile.write(str(temp))

myFile.close() # yazma işlemi bitti
#dosya tekrar açılıyor ve okunan değerler metin değişkenine atanıyor
dosya = open("numbers.txt")
metin = dosya.read()
#ozet alma kısmı
m = hashlib.md5() #m hash dosyamiz olusturuldu

for i in metin: # metinin her bir karakteri icin ozet alma fonksiyonu calistiriliyor.
	m.update(i.encode('utf-8'))
	ozet = m.hexdigest()
	y.append(ozet[7]) #ozetin 7.karakteri y dizisine ekleniyor

for k in range(len(y)):
	
	temp2 = y[k]
	y[k] = int(temp2, 16)
	
for j in y:
	print (j) 



