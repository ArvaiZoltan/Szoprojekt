import sqlite3
import random

def vélszám():
    véletlen=random.Random()
    return véletlen.randrange(2)

def rekord(list,x):
    return list[x]

def adat(list,x,y):
    return list[x][y]

adatbázis=sqlite3.connect("tanulók.db")

toll=adatbázis.cursor()
toll.execute("DROP TABLE IF EXISTS tanulók")
toll.execute("CREATE TABLE tanulók(név, szülév, átlag)")

toll.execute(""" INSERT INTO tanulók VALUES
    ('Mikorka Kálmán', 2000, 2.8),
    ('Víz Elek', 1995, 4.6) """)

adatbázis.commit()
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
