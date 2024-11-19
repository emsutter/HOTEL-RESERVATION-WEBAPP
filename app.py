from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def home():

    return render_template('home.html', endpoint=request.endpoint)

@app.route('/NuestrosHoteles')

def NuestrosHoteles():

    return render_template("NuestrosHoteles.html", endpoint=request.endpoint)

@app.route('/Galeria')

def Galeria():

    return render_template("Galeria.html", endpoint=request.endpoint)

@app.route('/Reservas')

def Reservas():

    return render_template("Reservas.html", endpoint=request.endpoint)

@app.route('/ConsultaReserva')

def ConsultaReserva():

    return render_template("ConsultaReserva.html", endpoint=request.endpoint)

@app.route('/contact')

def contact():

    return render_template("contact.html", endpoint=request.endpoint)

@app.route('/registro')

def registro():

    return render_template("registro.html", endpoint=request.endpoint)

if __name__ == "__main__":
    app.run("127.0.0.1", port="8080", debug=True)