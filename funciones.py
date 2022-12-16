import sqlite3 as sql

def get_db():
	conexion = sql.connect('base.db')
	return conexion

def registrar(query, datos):
	db = get_db()
	cur = db.cursor()
	cur.execute(query, datos)
	db.commit()
	db.close()

def consultar(query):
	db = get_db()
	cur = db.cursor()
	cur.execute(query)
	lista = cur.fetchall()
	db.commit()
	db.close()
	return lista


db = get_db()
cur = db.cursor()
cur.execute("drop table if exists destinos")
db.commit()
db.close()

db = get_db()
cur = db.cursor()
cur.execute("create table if not exists destinos(lugar text not null, naturaleza text not null, caminata text not null, montaña text not null, cultura text not null, playa text not null)")
db.commit()
db.close()


lista = [('MINCA', 'si', 'si', 'si', 'si', 'no'), ('POZO AZUL', 'si', 'si', 'si', 'no', 'no'), ('PALOMINO', 'si', 'no', 'no', 'si', 'si'), ('PARQUE TAYRONA', 'si', 'si', 'si', 'si', 'si'), ('CABO SAN JUAN', 'si', 'si', 'si', 'si', 'si'), ('CIUDAD PERDIDA', 'si', 'si', 'si', 'si', 'no'), ('PLAYA BLANCA', 'si', 'no', 'no', 'no', 'si'), ('SANTA MARTA', 'si', 'si', 'si', 'si', 'no')]
for i in range(len(lista)):
	registrar("insert into destinos(lugar, naturaleza, caminata, montaña, cultura, playa) values(?,?,?,?,?,?)", lista[i])