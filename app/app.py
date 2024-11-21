from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)


API_URL = 'http://127.0.0.1:5000/'


def generacion(url,template):
    """envia los datos del form a la ruta especifica de la API, 
    luego recibe la respuesta de la api y la rederiza al template indicado.
    En caso de que todavia no se haya enviado el form, se renderiza el template, siendo la respuesta de tipo None"""
        
    respuesta = None

        #verifica que se haya enviado el cuestionario
    if request.method == "POST":
        try:            
            datos = request.form.to_dict()

            for data in datos:

                if datos[data] == "":
                    return render_template(template, respuesta={"error": "Por favor, completa todos los campos."})
                
            #le envia los datos del form a la api, esta le devuelve un diccionario con un error o un mensaje de exito
            response = requests.post(url, json = datos)

                #si todo esta ok devuelve el diccionario con mensaje ok
            if response.status_code == 200:
                    
                    respuesta = response.json()  
            else:
                    #la API tiro un error
                    error = response.json().get('error', 'Hubo un problema. Por favor, intente de nuevo.')
                    respuesta = {"error": error}
            
            #hubo un problema enviando el cuestionario
        except requests.exceptions.RequestException as e:
        
            respuesta = {"error": f"Hubo un error al hacer la solicitud: {str(e)}"}
            

        #todavia no se hizo el cuestionario
    return render_template(template,respuesta=respuesta)


def get_informacion(tipo):
    """pide informacion de la base de datos a la API, devuelve la informacion o un error, el parametro es de tipo str y es un url"""

    try:
            #le pide a la API lo que necesite
        response = requests.get(tipo)
            #si esta todo ok devuelve un diccionario con los datos
        if response.status_code == 200:

            return response.json(), 200
        else:
           #si no encuentra lo que se pide devuelve un 404
           return {"error": "No se encontró"}, 404
        
        #error del servidor
    except requests.exceptions.RequestException as e:
         return {"error": f"Ha ocurrido un error en el servidor: {str(e)}"}, 500


def consultas_de_reserva(tipo):
    
    """envia los datos del form a la ruta especifica de la API, 
    luego llama a get_informacion para que pida la reserva especifica a la API"""

    datos = request.form.to_dict()

    if not "num_reserva" in datos:
        return {"error": "ingrese otro numero de reserva"}
    
    id = datos['num_reserva']

    url = f'{API_URL}/{tipo}/{id}'
   
    return get_informacion(url)

@app.route('/')

def home():

    return render_template('home.html', endpoint=request.endpoint)

@app.route('/NuestrosHoteles')

def NuestrosHoteles():
    #hay que traerlo de la base de datos

    """renderiza la pestania de consultas de nuestros hoteles. Devuelve un diccionario
    con los datos de los hoteles incluidos las url de las imagenes o un "error" si algo fallo"""

    tipo = ...  #falta el endpoint en la api

    url = API_URL + str(tipo)

    hoteles = get_informacion(url)

    return render_template("NuestrosHoteles.html", endpoint=hoteles)

@app.route('/Galeria')

def Galeria():

    """renderiza la pestania de galeria"""
    #hay que traer imagenes de la base de datos

    tipo = ...  #falta el endpoint en la api

    url = API_URL + str(tipo)

    habitaciones = get_informacion(url)

    return render_template("Galeria.html", habitaciones=request.endpoint)

@app.route('/Reservas')

def Reservas():
    """llama a la funcion generacion pasando por parametro la url a la ruta especifica de la API 
    y el template a renderizar para generar una reserva y rendrizar el template
    . retorna un diccionario con variable "mensaje", que trae un mensaje de exito
    o si sufrio un error un diccionario con variable "error' en caso de error"""

    url = API_URL + 'cliente_reserva'
    
    return generacion(url,'Reservas.html')

@app.route('/ConsultaReserva', methods=["GET", "POST"])

def ConsultaReserva():
    """renderiza la pestania de consultas de reserva. En caso de que el usuario haya completado el form, devuelve un diccionario
    con los datos de la reserva o un "error". En caso de que no haya completado el formulario la respuesta sera None """
    reserva = None

    #verifica que se haya enviado el cuestionario
    if request.method == "POST":  
        reserva = consultas_de_reserva("consultar_reserva")  

    
    return render_template("ConsultaReserva.html", endpoint=reserva)

@app.route('/contact')

def contact():

    """renderiza la pestania de contacto"""
    #agregar api de wsp para cuando se envie el formulario todo derive en un mensaje de wsp a la atencion al cliente del hotel
    #agregar api de maps para ver las distitnas ubicaciones del hotel

    return render_template("contact.html", endpoint=request.endpoint)

@app.route('/registro', methods = ["POST"])

def registro():

    """llama a la funcion generacion pasando por parametro la url a la ruta especifica de la API 
    y el template a renderizar. Devuelve un mensaje diccionario con un "error" si falla o un diccionario con un "mensaje"
    de exito"""

    url = API_URL + 'registrarse'

    return generacion(url,'...' )


#------------------------------------------------------------------------------------

#VISTAS QUE FALTAN CREAR:
    #registro, sirve para registrar al usuario
    #mi_usuario, sirve para que el usuario pueda ver todas sus reservas y servicios contratados
    #(NO OBLIGATORIO) vista para la cantidad de servicios a contratar 
    #(NO OBLIGATORIO) vista para eliminar reserva. 
    





if __name__ == "__main__":
    app.run("127.0.0.1", port="8080", debug=True)