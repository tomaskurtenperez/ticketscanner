from PIL import Image
import io

imagen = Image.open('test.png')

with io.BytesIO() as output:
    imagen.save(output, format='PNG')
    imagen_bytes = output.getvalue()

import mysql.connector

# Configura los datos de conexión
conexion = mysql.connector.connect(
    host="localhost",      # Por lo general, "localhost" si es local
    user="root",
    password="",
    database="scanner"
)

# Crea un cursor para interactuar con la base de datos
cursor = conexion.cursor()

datos = {
  'id': 1,
  'nombre': "farmacia",
  'tipo': "png",
  'imagen': imagen_bytes,
}
query = ("INSERT INTO tickets "
              "(id,nombre,tipo,imagen) "
              "VALUES (%(id)s, %(nombre)s, %(tipo)s, %(imagen)s)")
cursor.execute(query, datos)
# Ejecuta la consulta SQL con los valores de los campos
# cursor.execute('INSERT INTO `scanner`.`tickets` (id,nombre,tipo,imagen) VALUES (?,?,?, ?)', (1,'test.jpg','jpg' ,imagen_bytes))

# Guarda los cambios en la base de datos
conexion.commit()

# Cierra el cursor y la conexión
cursor.close()
conexion.close()



