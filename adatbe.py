import sqlite3


adatbázis=sqlite3.connect("próba.db")

toll=adatbázis.cursor()
toll.execute("DROP TABLE IF EXISTS tanulók")
toll.execute("CREATE TABLE tanulók(név, szülév, átlag)")

nev=input('Mi legyen a név?')
szülev=int(input('Szülév:'))
atlag=int(input('Átlag:'))

toll.execute(""" INSERT INTO tanulók VALUES
    ('Mikorka Kálmán', 2000, 2.8),
    ('Víz Elek', 1995, 4.6) """)

adatbázis.commit()

for adatok in toll.execute("SELECT név, szülév FROM tanulók ORDER BY szülév"):
    print (adatok)

adatbázis.close()
    


