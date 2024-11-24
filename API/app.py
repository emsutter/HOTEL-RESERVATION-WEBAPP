from flask import Flask, jsonify, request
import consultas

app = Flask(__name__)


def metodo_post(funcion):

    """recibe los datos enviados desde el app.py del front y maneja los casos de tipo POST, en los cuales hay que agregar datos en la base de datos. 
    Como agregando un usuario o una reserva"""
     
    if request.method == "POST":
        try:

            respuesta = request.get_json()
            

            for variables in respuesta:
                
                if respuesta[variables] == "":
                    
                    return jsonify({"error": "Datos incompletos, asegúrate de enviar todo" }), 400

            funcion(respuesta)

            return jsonify({"mensaje": "se ha  creado correctamente"}), 202
        
        except Exception as e:
            return jsonify({"error": f"Ocurrió un error: {str(e)}"}), 500 

    
    return jsonify({"error": "no se envio el cuestionario"}), 405

def metodo_get(funcion, id):
    """maneja los casos de tipo GET y DELETE, buscando la informacion que se necesita de la base de datos o elminando la reserva especificada """
    try:
        
        data = funcion(id)

        if data is not None:

            if data ==  True:
                return jsonify({"mensaje": "Reserva eliminada correctamente"}), 200
            
            else:
                return jsonify(data), 200
            
        else:
            return jsonify({"error": "Reserva no encontrada"}), 404
        
    except Exception as e:
            return jsonify({"error": f"Ocurrió un error: {str(e)}"}), 500 


def get_todos(funcion):
    """maneja los casos donde hay que traer todo lo que esta en la tabla"""

    try:

        data = funcion()

        return jsonify(data), 200
    
    except Exception as e:
            return jsonify({"error": f"Ocurrió un error: {str(e)}"}), 500

    

@app.route('/cliente_reserva', methods = ["POST"])

def cliente_reserva():
    """llama a la funcion metodo post para agregar una reserva en la base de datos"""

    return metodo_post(consultas.Insertar_reserva)


@app.route('/consultar_reserva/<int:id>', methods = ["GET"])

def consultar_reserva(id):
    """recibe el id de reserva enviado desde el app.py del front
    y llama a la funcion metodo get para consultasr reserva por ID de reserva"""

    return metodo_get(consultas.Reserva_by_id, id)



@app.route('/eliminar_reserva/<int:id>', methods = ["DELETE"])

def eliminar_reserva(id):
    """recibe el id de reserva enviado desde el app.py del front
    y llama a la funcion metodo get para eliminar la reserva por ID de reserva"""

    return metodo_get(consultas.Borrar_reserva, id)

     

@app.route('/registrarse', methods = ['POST'])

def registarse():
    """llama a la funcion metodo post crear un usuario en la base de datos"""

    return metodo_post(consultas.insertar_usuario)


@app.route('reservas_por_usuario<str:mail>', methods = ["GET"])

def reservas_por_usuario(mail):
    """recibe el mail del usuario enviado desde el app.py del front
    y llama a la funcion metodo get para mostrar las reservas del usuario"""

    return metodo_get(consultas.Reserva_del_usuario, mail)
    
@app.route('obtener_hoteles', methods = ["GET"] ) 

def obtener_hoteles():

    return get_todos(consultas.obtener_hoteles())

@app.route('obtener_habitaciones', methods = ["GET"] ) 

def obtener_habitaciones():

    return get_todos(consultas.obtener_habitaciones())


@app.route('obtener_reservas', methods = ["GET"] ) 

def obtener_reservas():

    return get_todos(consultas.obtener_reservas())


@app.route('obtener_servicios', methods = ["GET"] ) 

def obtener_servicios():

    return get_todos(consultas.obtener_servicios())


@app.route('obtener_usuarios', methods = ["GET"] ) 

def obtener_usuarios():

    return get_todos(consultas.obtener_usuarios())




##que falta

#GET PARA TRAER HOTELES DE LA BASE DE DATOS
#GET PARA LAS HAITACIONES O PARA TRAER LA PARTE DE GALERIA
#POST PARA CONTRATAR UN SERVICIO
#DELETE PARA ELIMINAR UN SERVICIO








            


        

if __name__ == "__main__":
    app.run("127.0.0.1", port="5000", debug=True)