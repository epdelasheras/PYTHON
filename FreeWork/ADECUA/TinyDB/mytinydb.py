from tinydb import TinyDB, Query

db = TinyDB('db.json')

#throw away all data to start with an empty database
db.truncate()
db.all()
db.drop_tables() #trhow away the table.

# create a table in the db
table = db.table('Pisos')

#insert items in default table
db.insert({'Nombre': 'Enrique', 'DNI': '53442925X'})
db.insert({'Nombre': 'Juan', 'DNI': '3064834Z'})

#insert items in pisos table
#table.insert({'Id': '1', 'Picname': 'DB-P1-00-LC1A'})
#table.insert({'Id': '2', 'Picname': 'V1-P1-00&01B-DUPLEX_3MF_0D.A_DA&3MF_2D.1_DA'})

User=Query()
el = db.get(User.Nombre == "Enrique")
print(el.doc_id)
table.insert({'Id': 'el.doc_id', 'Picname': 'DB-P1-00-LC1A'})

print(table.all())