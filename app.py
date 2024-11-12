from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def home():

    return render_template('home.html')

@app.route('/ConsultaReserva')

def ConsultaReserva():

    return render_template("ConsultaReserva.html")

@app.route('/Reservas')

def Reservas():

    return render_template("Reservas.html")

@app.route('/contact')

def contact():

    return render_template("contact.html")

@app.route('/Galeria')

def Galeria():

    return render_template("Galeria.html")

@app.route('/NuestrosHoteles')

def NuestrosHoteles():

    return render_template("NuestrosHoteles.html")

if __name__ == "__main__":
    app.run("127.0.0.1", port="8080", debug=True)