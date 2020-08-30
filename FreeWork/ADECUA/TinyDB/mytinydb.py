from tinydb import TinyDB, Query

db = TinyDB('db.json')

#throw away all data to start with an empty database
db.truncate()
db.all()

#insert items
db.insert({'Nombre': 'Enrique', 'Piso': 'DB-P3-02-2MP_1D.A'})
db.insert({'Nombre': 'Jose', 'Piso': 'DB-P3-03_Atico-3MF_0D.C&3MF_3D.A1'})

#get all documents stored in the database
print (db.all())

#iter over stored documents
for item in db:
    print(item)