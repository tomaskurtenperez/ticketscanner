
import mysql.connector

# Configura los datos de conexión
conexion2 = mysql.connector.connect(
    host="localhost",      # Por lo general, "localhost" si es local
    user="root",
    password="",
    database="scanner"
)
cursor = conexion2.cursor()

query = ("SELECT * FROM `scanner`.`tickets` WHERE id=1")
cursor.execute(query)
resultados = cursor.fetchall()
# print(resultados[0][3])
conexion2.commit()
cursor.close()






from PIL import Image
import io

# Supongamos que tienes una imagen en bytes
imagen_en_bytes = resultados[0][3]

# Convierte los bytes en un objeto de imagen
imagen = Image.open(io.BytesIO(imagen_en_bytes))

# Ahora puedes trabajar con la imagen normalmente, por ejemplo, mostrarla
imagen.show()

imagen.save('imagen_recuperada.png')
