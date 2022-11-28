#uloha5
'''
import tkinter
canvas = tkinter.Canvas(width=300, height=320)
canvas.pack()

subor = open('clanok.txt', 'r',encoding = 'utf-8')
frekvencia = {}
for riadok in subor:
    riadok = riadok.lower()
    for znak in riadok:
        if 'a' <= znak <= 'z':
            frekvencia[znak] = frekvencia.get(znak, 0) + 1
subor.close()
zoradene = sorted(frekvencia, key=frekvencia.get, reverse=True)
for kluc in zoradene:
    print(kluc, frekvencia.get(kluc))

def kresli_stlpec(x, y, dx, dy, znaky):
    fa, fb = 'yellow', 'lightblue'
    for znak in znaky:
        canvas.create_rectangle(x, y, x+dx, y+dy, fill=fa)
        canvas.create_text(x+dx/2, y+dy/2, text=znak)
        y += dy
        fb, fa = fa, fb

velkost = 300
pocet_casti = 2
x = 10
y = 10
dx = 50
spracovat = zoradene[:]

while len(spracovat) > 0:
    kresli_stlpec(x, y, dx, velkost/pocet_casti, spracovat[:pocet_casti])
    spracovat = spracovat[pocet_casti:]
    x += dx
    pocet_casti *= 2
'''

#uloha6
'''
subor = open('clanok.txt', 'r',encoding = 'utf-8')
frekvencia = {}
p = 0
for riadok in subor:
    riadok = riadok.lower()
    for znak in riadok:
        if 'a' <= znak <= 'z':
            p+=1
            frekvencia[znak] = frekvencia.get(znak, 0) + 1
subor.close()
zoradene = sorted(frekvencia, key=frekvencia.get, reverse=True)
for kluc in zoradene:
    percento = (frekvencia.get(kluc)/p)*100
    print(kluc, frekvencia.get(kluc), '{:.2f}'.format(percento)+'%')
'''

#uloha7
'''
import tkinter
canvas = tkinter.Canvas(height=300,width=300,bg='white')
canvas.pack()
subor = open('clanok.txt', 'r',encoding = 'utf-8')
frekvencia = {}
x=20
for riadok in subor:
    riadok = riadok.lower()
    for znak in riadok:
        if 'a' <= znak <= 'z':
            frekvencia[znak] = frekvencia.get(znak, 0) + 1
subor.close()
zoradene = sorted(frekvencia, key=frekvencia.get, reverse=True)
canvas.create_line(20,290,280,290,width=2)
canvas.create_line(20,290,20,90,width=2)
for kluc in zoradene:
    #print(kluc, frekvencia.get(kluc))
    canvas.create_text(x+5,295,text=kluc)
    canvas.create_text(x+5,285-(frekvencia.get(kluc)*2),text=frekvencia.get(kluc),font='Arial 5')
    canvas.create_rectangle(x,290,x+10,290-(frekvencia.get(kluc)*2),fill='blue')
    x+=10
'''    
    
#uloha9,10
'''
import tkinter
canvas = tkinter.Canvas(width=1000, height=800)
canvas.pack()

subor = open('slovne_hodnotenia.txt', 'r',encoding='utf-8')
subor1 = open('vynimky.txt', 'r',encoding='utf-8')
subor2 = open('pocetnost.txt', 'w',encoding='utf-8')

vynimky = []
pocetnost = {}
p=0
for r in subor:
    r = r.replace(',', '')
    slova = r.split()
    for slovo in slova:
        pocetnost[slovo] = pocetnost.get(slovo, 0) +1
        p +=1

subor.close()
for riadok in subor1:
    vynimky = riadok.split()
subor1.close()
zoznam = []
for ntica in pocetnost.items():
    zoznam.append((ntica[1], ntica[0]))

zoznam.sort(reverse=True)

kopia = []
for prvok in zoznam:
    if len(prvok[1]) >= 3 or prvok[1] in vynimky:
        kopia.append(prvok)
    percento =  (prvok[0]/p)*100
    subor2.write(prvok[1]+';'+str(prvok[0])+';'+str(percento)+'%'+'\n')
subor2.close()
def obdlznik(poradie, vyska, farba):
    canvas.create_rectangle(poradie*20+10, maxy-100, poradie*20+10+10,
                            maxy-100-vyska//2, fill=farba,
                            tags='obdlznik'+str(poradie))

poradie = 0
maxy = 800

for pocet, slovo in kopia[:40]:
    obdlznik(poradie, pocet, 'blue')
    canvas.create_text(poradie*20+15, maxy-50, text=slovo,
                        font='Arial 8', angle=90)
    poradie += 1

def mys(sur):
    global rozsvietene
    if rozsvietene != None:
        canvas.delete('obdlznik'+str(rozsvietene))
        obdlznik(rozsvietene, kopia[rozsvietene][0], 'blue')
    canvas.delete('info')
    if sur.y < 700 and 10 < sur.x < 40*20:
        ktory = (sur.x-10)//20
        canvas.delete('obdlznik'+str(ktory))
        obdlznik(ktory, kopia[ktory][0], 'red')
        canvas.create_text(500, 100, text=kopia[ktory][1]+'\n '
                            +str(kopia[ktory][0]), font='Arial 30',
                            tags='info')
        rozsvietene = ktory

rozsvietene = None
canvas.bind('<Motion>', mys)
'''

#uloha11
'''
import random
subor = open('slovne_hodnotenia.txt', 'r',encoding='utf-8')
celytext = subor.read()
celytext = celytext.split()
subor.close()

slova = []
for slovo in celytext:
    if not slovo in slova:
        slova.append(slovo)
slova_zamiesane = slova[:]


random.shuffle(slova_zamiesane)

substitucia = {}
for i in range(len(slova)):
    substitucia[slova[i]] = slova_zamiesane[i]

celytext_sifrovany = ''
for slovo in celytext:
    celytext_sifrovany = celytext_sifrovany + substitucia[slovo]

subor_sifrovany = open('slovne_hodnotenia_sifrovane.txt', 'w')
subor_sifrovany.write(celytext_sifrovany)
subor_sifrovany.close()

subor_tabulka = open('slovne_hodnotenia_kluc.txt', 'w')
for kluc, hodnota in substitucia.items():
    subor_tabulka.write(kluc+';'+hodnota+';')
subor_tabulka.close()
'''

#uloha12
'''
import tkinter
from random import *
canvas= tkinter.Canvas(width=800, height=600, bg='white')
canvas.pack()

subor=open('clanok.txt','r', encoding='utf-8')

pocetnost={}

for r in subor:
    r=r.replace(',','')
    slova=r.split()
    for slovo in slova:
        pocetnost[slovo]=pocetnost.get(slovo,0)+1
subor.close()

zoznam=[]
for ntica in pocetnost.items():
    zoznam.append((ntica[1],ntica[0]))

zoznam.sort(reverse=True)

kopia=[]
for prvok in zoznam:
    if len(prvok[1])>=3:
        kopia.append(prvok)

kopia=kopia[:40]

poradie=0
maxy=800

def rgb(r,g,b):
    return '#{:02x}{:02x}{:02x}'.format(r,g,b)

for pocet,slovo in kopia[::-1]:
    velkost=poradie+5
    x=randint(100,700)
    y=randrange(100,500)
    farba=rgb(randrange(256),randrange(256),randrange(256))
    uhol=randint(-90,90)
    canvas.create_text(x,y,text=slovo, font=('Arial',velkost),angle=uhol, fill=farba)
    poradie+=1
'''

#uloha13
'''
subor = open('osoby.txt', 'r')
menar = []
menam = []
r = int(input('Zadaj rok:'))
m = input('Zadaj mesto:')
for riadok in subor:
    info = riadok.split(';')
    if int(info[2]) == r:
        menar.append(info[0])
    if info[3].strip() == m:
        menam.append(info[0])
subor.close()
print('Osoby narodene v meste',m,'sú',menam)
print('Osoby narodene v roku',r,'sú',menar)
'''

#uloha14
'''
subor = open('osoby.txt', 'r')
vyska = 0
vek = 1000
for riadok in subor:
    info = riadok.split(';')
    if 2022-int(info[2]) < vek:
        vek = 2022-int(info[2])
        ovek = info[0]
    if int(info[1]) > vyska:
        vyska = int(info[1])
        ovys = info[0]
subor.close()
print('Najvyššia osoba je',ovys)
print('Najmladšia osoba je',ovek)
'''

#uloha15
'''
subor = open('eu_sk.csv','r')
obyvatelia = 0
p=0
rozloha = 0
m = ''
for riadok in subor:
    p+=1
    riadok = riadok.replace(',','.')
    riadok = riadok.replace(' ','')
    riadok = riadok.strip()
    riadok = riadok.split(';')
    obyvatelia += float(riadok[2])
    if int(riadok[3]) > rozloha:
        rozloha = int(riadok[3])
        m = riadok[0]
obyvatelia = obyvatelia/p    
subor.close()
print('Priemerný počet obyvateľov je',obyvatelia,'miliónov.')
print('Najväčšiu rozlohu má',m,'a je',rozloha)
'''

#uloha16