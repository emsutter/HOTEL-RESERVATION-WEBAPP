from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
import consultas
from flask_mail import Mail, Message
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/apc_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['MAIL_SERVER'] = 'smtp.gmail.com' 
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'marcomasciullidev@gmail.com' 
app.config['MAIL_PASSWORD'] = 'cisx vxak ezgy htga'
app.config['MAIL_DEFAULT_SENDER'] = 'noreply@argentinaporcolpinto.com'

mail = Mail(app)
db = SQLAlchemy(app)

@app.route('/')
def home():
    imagenes = consultas.obtener_imagenes()
    return render_template('home.html', imagenes=imagenes, endpoint=request.endpoint)

@app.route('/NuestrosHoteles')
def NuestrosHoteles():
    hoteles = consultas.obtener_hoteles_con_imagen()
    return render_template("NuestrosHoteles.html", hoteles=hoteles, endpoint=request.endpoint)

@app.route('/Galeria')
def Galeria():
    imagenes = consultas.obtener_imagenes()
    return render_template("Galeria.html", imagenes=imagenes, endpoint=request.endpoint)

@app.route('/Reservas')
def Reservas():
    hoteles = consultas.obtener_hoteles()
    hotel_id = request.args.get('hotel_id')
    
    return render_template("Reservas.html", hoteles=hoteles, hotel_id=hotel_id, endpoint=request.endpoint)

@app.route('/ConsultaReserva')
def ConsultaReserva():
    return render_template("ConsultaReserva.html", endpoint=request.endpoint)

@app.route('/contact')
def contact():
    return render_template("contact.html", endpoint=request.endpoint)

@app.route('/admin')
def admin():
    hoteles = consultas.obtener_hoteles()
    habitaciones = consultas.obtener_habitaciones()
    reservas = consultas.obtener_reservas()
    servicios = consultas.obtener_servicios()
    usuarios = consultas.obtener_usuarios()

    return render_template('admin.html', hoteles=hoteles, habitaciones=habitaciones, reservas=reservas, servicios=servicios, usuarios=usuarios)

@app.route('/admin/agregar_hotel', methods=['POST'])
def agregar_hotel():
    try:
        data = request.get_json()
        if 'nombre' not in data:
            return jsonify({"error": "El campo 'nombre' es obligatorio"}), 400
        
        nombre = data['nombre']
        descripcion = data['descripcion']
        ubicacion = data['ubicacion']

        hotel_id = consultas.agregar_hotel(nombre, descripcion, ubicacion)
        
        imagenes = data.get('imagenes', [])
        if imagenes:
            consultas.agregar_imagenes(hotel_id, imagenes)
        

        nuevo_hotel = {"id": hotel_id, "nombre": nombre}
        return jsonify({"message": "Hotel agregado correctamente", "hotel": nuevo_hotel}), 201

    
    except Exception as e:
       
        print(f"Error al agregar el hotel: {str(e)}")
        return jsonify({"error": f"Error interno: {str(e)}"}), 500

@app.route('/admin/eliminar_hotel/<int:hotel_id>', methods=['DELETE'])
def eliminar_hotel(hotel_id):
    try:
        consultas.eliminar_hotel(hotel_id)
        return jsonify({"message": "Hotel eliminado correctamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/admin/agregar_habitacion', methods=['POST'])
def agregar_habitacion():
    try:
        data = request.get_json()
        
        if 'capacidad' not in data or 'hotel_id' not in data:
            return jsonify({"error": "Los campos 'capacidad' y 'hotel_id' son obligatorios"}), 400

        capacidad = data['capacidad']
        hotel_id = data['hotel_id']

        habitacion_id = consultas.agregar_habitacion(capacidad, hotel_id)

        nueva_habitacion = {
            "id": habitacion_id,
            "capacidad": capacidad,
            "hotel": {
                "id": hotel_id, 
                "nombre": "metodo obtener nombre hotel por id./admin/agregar_habitacion"
            }
        }

        return jsonify({"message": "Habitación agregada correctamente", "habitacion": nueva_habitacion}), 201
    
    except Exception as e:
        print(f"Error al agregar la habitación: {str(e)}")
        return jsonify({"error": f"Error interno: {str(e)}"}), 500

@app.route('/admin/agregar_servicio', methods=['POST'])
def agregar_servicio():
    try:
        data = request.json
        nombre = data['nombre']
        descripcion = data['descripcion']
        url_imagen = data['url_imagen']
        ubicacion = data['ubicacion']

        servicio_id = consultas.agregar_servicio(nombre, descripcion, url_imagen, ubicacion);

        nuevo_servicio = {
            "servicio_id": servicio_id,
            "nombre": nombre,
            "descripcion": descripcion,
            "url_imagen": url_imagen
        }

        return jsonify({"message": "Servicio agregado correctamente", "servicio": nuevo_servicio}), 201
    
    except Exception as e:
        print(f"Error al agregar la habitacion: {str(e)}")
        return jsonify({"error": f"Error interno: {str(e)}"}), 500

@app.route('/admin/agregar_reserva', methods=['POST'])
def agregar_reserva():
    try: 
        data = request.get_json()
        email = data.get('email')
        ingreso = data.get('ingreso')
        egreso = data.get('egreso')
        hotel_id = data.get('hotel_id')

        reserva_id = consultas.agregar_reserva(email, ingreso, egreso, hotel_id)
        enviar_correo(email, reserva_id, ingreso, egreso, hotel_id)
        return jsonify({'success': True, 'message': 'Reserva realizada con éxito'}), 200
    
    except Exception as e:
        print(f"Error al crear la reserva: {str(e)}")
        return jsonify({"error": f"Error interno: {str(e)}"}), 500


def enviar_correo(email, reserva_id, ingreso, egreso, hotel_id):
    try:
        # Definir el cuerpo del correo
        cuerpo_html = f"""
        <html>
            <head>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        color: #333;
                    }}
                    .header {{
                        text-align: center;
                    }}
                    .header img {{
                        max-width: 200px;
                    }}
                    .content {{
                        text-align: center;
                        margin-top: 20px;
                    }}
                    .button {{
                        background-color: #007bff;
                        color: white;
                        padding: 10px 20px;
                        text-decoration: none;
                        border-radius: 5px;
                        margin-top: 20px;
                    }}
                </style>
            </head>
            <body>
                <div class="header">
                    <!-- Referencia a la imagen adjunta por su CID -->
                    <img src="cid:logo_hotel" alt="Logo Hotel">
                    <h1>¡Tu reserva se ha realizado con éxito!</h1>
                </div>
                <div class="content">
                    <p>¡Hola! Nos complace informarte que tu reserva en nuestro hotel ha sido realizada con éxito.</p>
                    <p><strong>Detalles de tu reserva:</strong></p>
                    <p><strong>ID de Reserva:</strong> {reserva_id}</p>
                    <p><strong>Fecha de Ingreso:</strong> {ingreso}</p>
                    <p><strong>Fecha de Egreso:</strong> {egreso}</p>
                    <p><strong>Hotel:</strong> {hotel_id}</p>
                </div>
            </body>
        </html>
        """

        # Crear el mensaje
        msg = Message("Confirmación de tu reserva", recipients=[email])
        msg.html = cuerpo_html

        # Adjuntar el logo como imagen
        with app.open_resource("static/images/logo_hotel.png") as logo:
            msg.attach(
                "logo_hotel.png",  # Nombre del archivo
                "image/png",  # Tipo MIME de la imagen
                logo.read(),  # Contenido de la imagen
                headers={"Content-ID": "<logo_hotel>"}  # Este es el CID que usaremos en el HTML
            )

        # Enviar el correo
        mail.send(msg)  # Asegúrate de que 'mail' esté correctamente inicializado
        print("Correo enviado con éxito")

    except Exception as e:
        print(f"Error al enviar el correo: {str(e)}")

    
if __name__ == "__main__":
    app.run("127.0.0.1", port="5000", debug=True)
