#main.py
import sqlite3
#coneccion
con = sqlite3.connect('crud.db')
cur = con.cursor()

#insertar
#person = ('Lucas', 'Vera', '235454666', 'Av Carpio')
#cur.execute('insert into person (name, lastname, phone, address) values (?,?,?,?)', person)
#con.commit()

#actualizar
person = ('Manuel', 'Carpio', '235454666', 'Av Carpio', 1)
cur.execute('update person set name=?, lastname=?, phone=?, address=? where id=?', person)
con.commit()

#eliminar
#cur.execute('delete from person where id=?', ('1'))
#con.commit()

#listar
for p in cur.execute('select * from person'):
    print (p)