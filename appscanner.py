from flask import Flask,render_template,request, redirect, send_from_directory

# Importamos el módulo que permite conectarnos a la BS
from PIL import Image
import io
from flaskext.mysql import MySQL
#--------------------------------------------------------------------
# Creamos la aplicación
app = Flask(__name__)
#--------------------------------------------------------------------
# Creamos la conexión con la base de datos:
mysql = MySQL()
# Creamos la referencia al host, para que se conecte a la base
# de datos MYSQL utilizamos el host localhost
app.config['MYSQL_DATABASE_HOST']='localhost'
# Indicamos el usuario, por defecto es user
app.config['MYSQL_DATABASE_USER']='root'
# Sin contraseña, se puede omitir
app.config['MYSQL_DATABASE_PASSWORD']=''
# Nombre de nuestra BD
app.config['MYSQL_DATABASE_BD']='scanner'
# Creamos la conexión con los datos
mysql.init_app(app) 

@app.route('/')
def index():

 sql = "SELECT * FROM `scanner`.`tickets`;"

 conn = mysql.connect()

 cursor = conn.cursor()

 cursor.execute(sql)

 db_tickets = cursor.fetchall()

 conn.commit()

 return render_template('tickets/index.html',tickets = db_tickets)



# @app.route('/create')
# def create():
#  return render_template('tickets/create.html')


# @app.route('/store', methods=['POST'])
# def storage():
#  # Recibimos los valores del formulario y los pasamos a variables locales:
#  _nombre = request.form['txtNombre']
#  _correo = request.form['txtCorreo']
#  _foto = request.files['txtFoto']

#  # Y armamos una tupla con esos valores:
#  datos = (_nombre,_correo,_foto.filename)

#  # Armamos la sentencia SQL que va a almacenar estos datos en la DB:
#  sql = "INSERT INTO `scanner`.`tickets` \
#  (`id`, `nombre`, `correo`, `foto`) \
#  VALUES (NULL, %s, %s, %s);"
#  conn = mysql.connect() # Nos conectamos a la base de datos
#  cursor = conn.cursor() # En cursor vamos a realizar las operaciones
#  cursor.execute(sql, datos) # Ejecutamos la sentencia SQL en el cursor
#  conn.commit() # Hacemos el commit
#  return render_template('tickets/index.html') # Volvemos a index.html


@app.route('/upload', methods=['POST'])
def storage():
    # Recibimos los valores del formulario y los pasamos a variables locales:
    # _nombre = request.form['txtNombre']

    imagen = request.files['imagen']

    imagen_bytes = imagen.read()
    
    # Y armamos una tupla con esos valores:

    # Armamos la sentencia SQL que va a almacenar estos datos en la DB:
    # conexion = mysql.connector.connect(
    #     host="localhost",      # Por lo general, "localhost" si es local
    #     user="root",
    #     password="",
    #     database="scanner"
    # )

    # Crea un cursor para interactuar con la base de datos
    conn = mysql.connect()

    cursor = conn.cursor()

    datos = {
    'nombre': "ticketsuper",
    'tipo': "jpeg",
    'imagen': imagen_bytes,
    }

    query = ("INSERT INTO `scanner`.`tickets` "
                "(nombre,tipo,imagen) "
                "VALUES (%(nombre)s, %(tipo)s, %(imagen)s)")
    cursor.execute(query, datos)
    conn.commit()

    cursor.close()
    conn.close()
    return render_template('tickets/create.html')

@app.route('/create')
def create():
 return render_template('tickets/create.html')

# @app.route('/upload', methods=['GET', 'POST'])
# def upload():
#     if request.method == 'POST':
#         # Obtén la imagen del formulario
#         imagen = request.files['imagen']

#         if imagen:
#             # Convierte la imagen a bytes
#             imagen_bytes = imagen.read()
            
#             # Procesa la imagen utilizando la biblioteca PIL
#             img = Image.open(io.BytesIO(imagen_bytes))

#             # Haz algo con la imagen, por ejemplo, mostrarla
#             img.save('imacrud.png')

#     return render_template('tickets/create.html')

if __name__=='__main__':
 app.run(debug=True)