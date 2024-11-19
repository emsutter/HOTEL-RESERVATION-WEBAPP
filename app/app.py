from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)


API_URL = 'http://127.0.0.1:5000/'


def generacion(url,template):
    """envia los datos del form a la ruta especifica de la API, 
    luego recibe la respuesta de la api y la rederiza al template indicado.
    En caso de que todavia no se haya enviado el form, se renderiza el template, siendo la respuesta de tipo None"""
        
    respuesta = None

        
    if request.method == "POST":
        try:            
            datos = request.form.to_dict()

            for data in datos:

                if datos[data] == "":
                    return render_template(template, respuesta={"error": "Por favor, completa todos los campos."})
                

            response = request.post(url, json = datos)


            if response.status_code == 200:
                    
                    respuesta = response.json()  
            else:
                
                    respuesta= {"error": "Hubo un problema. Por favor, intente de nuevo."}
            
        except requests.exceptions.RequestException as e:
        
            respuesta = {"error": f"Hubo un error al hacer la solicitud: {str(e)}"}
            

   
    return render_template(template,respuesta=respuesta)


def consultas(tipo):
    
    """envia los datos del form a la ruta especifica de la API, 
    luego recibe la respuesta de la api y devuelve un json con un error o con
    la respuesta esperada de la api"""

    datos = request.form.to_dict()
    
    for data in datos:
        id = datos[data]

    url = f'{API_URL}/{tipo}/{id}'

    response = request.post(url)

    if response.status.code == 200:

        return jsonify(response.json()), 200
    else:
        return jsonify({"error": "No se encontro la el usuario o la reserva"}), 404
            

@app.route('/')

def index():
    """renderiza el home de la pagina"""

    return render_template('index.html')

@app.route('/about')

def about():
    """renderiza la ventana about de la pagina"""

    return render_template("about.html")

@app.route('/blog')

def blog():
    """renderiza la parte de blog de la pagina"""

    return render_template("blog.html")

@app.route('/contact')


def contact():
    """renderiza la parte de contacto de la pagina"""


    return render_template("contact.html")


@app.route('/Reserva', methods = ["POST"])

def reserva():
    """llama a la funcion generacion pasando por parametro la url a la ruta especifica de la API 
    y el template a renderizar"""

    url = API_URL + 'cliente_reserva'
    
    return generacion(url,'reserva.html')


@app.route('/registro', methods = ["POST"])

def registro():

    """llama a la funcion generacion pasando por parametro la url a la ruta especifica de la API 
    y el template a renderizar."""

    url = API_URL + 'registrarse'

    return generacion(url,'reserva.html' )


       






if __name__ == "__main__":
    app.run("127.0.0.1", port="8080", debug=True)