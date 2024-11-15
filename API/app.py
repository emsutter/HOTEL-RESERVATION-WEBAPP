from flask import Flask, jsonify, request
import consultas

app = Flask(__name__)

API_URL = 'http://127.0.0.1:5000'

@app.route('/cliente_reserva', methods = ["GET", "POST"])

def cliente_reserva():
    """recibe el post del form de reserva y envia 
    un post a la base de datos donde crea la reserva"""

    if request.method == "POST":
        try:

            reserva = request.get_json()
            datos_necesarios = []

            for variables in reserva:
                
                if reserva[variables] == "":
                    
                    return jsonify({"error": "Datos incompletos, asegúrate de enviar todo" }), 400

            consultas.insertar_reserva(reserva)

            return jsonify({"mensaje": "Reserva creada correctamente"}), 202
        
        except Exception as e:
            return jsonify({"error": f"Ocurrió un error: {str(e)}"}), 500 

    
    return jsonify({"error": "no se envio el cuestionario"}), 405


@app.route('/consultar_reserva/<int:id>', methods = ["GET"])

def consultar_reserva(id):
    """consulta reserva por ID de reserva"""

    if request.method == "GET":
        try:
            
            reserva = consultas.reserva_by_id(id)

            if not reserva:
                return jsonify({"error": "la reserva ingresada no existe"}), 404
            

            return jsonify(reserva), 200
        
        except Exception as e:
            return jsonify({"error": f"Ocurrió un error: {str(e)}"}), 500

@app.route('/eliminar_reserva/<int:id>', methods = ["DELETE"])

def eliminar_reserva(id):

        """elimina una reserva por su ID"""

        try:

            reserva = consultas.borrar_reserva(id)

            if not reserva:
                return jsonify({"error": "la reserva ingresada no existe"}), 404
            
        except Exception as e:
            return jsonify({"error": f"Ocurrió un error: {str(e)}"}), 500
        


@app.route('/mostrar_listado_reservas', methods = ["GET"])

def mostrar_listado_reservas():
    """envia todas las reservas en formato JSON"""

    if request.method == "GET":
        try:

            reservas = consultas.Mostrar_reservas()

            if not reservas:
                return jsonify({"error": "No se ha hecho ninguna reserva"}), 404 

            return jsonify(reservas) 
            
        except Exception as e:
            return jsonify({"error": f"Ocurrió un error: {str(e)}"}), 500

            


        

if __name__ == "__main__":
    app.run("127.0.0.1", port="5000", debug=True)