import sqlite3
import random

def vélszám():
    véletlen=random.Random()
    return véletlen.randrange(2)

def rekord(list,x):
    return list[x]

def adat(list,x,y):
    return list[x][y]

adatbázis=sqlite3.connect("próba.db")
toll=adatbázis.cursor()

listad=[]
for adatok in toll.execute("SELECT név, szülév FROM tanulók ORDER BY szülév"):
    print (adatok)
    listad.append(adatok)   
adatbázis.close()

vél=vélszám()
print(vél)
print (rekord(listad,0))
print (adat(listad,0,1))
print (adat(listad,vél,0))
