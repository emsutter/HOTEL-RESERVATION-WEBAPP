from flask import Flask, render_template, request
import requests

app = Flask(__name__)


API_URL = 'http://127.0.0.1:5000/'

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


@app.route('/Reserva')

def reserva():
    """muestra el template reserva.html, donde le pasa el url de la api para el form y envia el diccionario data 
    para mostrar el mensaje de cuando termina el form, envia none si todavia no se envio el formulario """

    url = API_URL + 'cliente_reserva'
    data = None
    

    if  request.method == 'POST':
        #para verificar que se haya enviado el fomulario
        try:
        
            response = requests.post(url)  
            
        
            if response.status_code == 200:
                
                data = response.json()  
            else:
            
                data = {"error": "Hubo un problema con la reserva. Por favor, intente de nuevo."}
            
        except requests.exceptions.RequestException as e:
        
            data = {"error": f"Hubo un error al hacer la solicitud: {str(e)}"}
            

   
    return render_template('reserva.html', url=url, data=data)



if __name__ == "__main__":
    app.run("127.0.0.1", port="8080", debug=True)