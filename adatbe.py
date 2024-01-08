import sqlite3

def adatbevitel():
    adatbázis=sqlite3.connect("próba.db")

    toll=adatbázis.cursor()
    toll.execute("CREATE TABLE IF NOT EXISTS tanulók(név, szülév, átlag)")

    nev=input('Mi legyen a név?')
    szülev=int(input('Szülév:'))
    atlag=int(input('Átlag:'))


    adat = (
        {"név": nev, "szülév": szülev, "átlag":atlag},
    )

    toll.executemany("INSERT INTO tanulók VALUES(:név, :szülév, :átlag)", adat)

    adatbázis.commit()

    for adatok in toll.execute("SELECT név, szülév FROM tanulók ORDER BY szülév"):
        print (adatok)

    adatbázis.close()

adatbevitel()
    


