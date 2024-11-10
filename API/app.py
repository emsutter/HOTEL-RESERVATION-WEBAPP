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

    
    return jsonify({"error": "Método no permitido, use POST"}), 405
        















if __name__ == "__main__":
    app.run("127.0.0.1", port="5000", debug=True)