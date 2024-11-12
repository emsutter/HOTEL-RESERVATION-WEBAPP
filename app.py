from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def home():

    return render_template('home.html')

@app.route('/about')

def about():

    return render_template("about.html")

@app.route('/blog')

def blog():

    return render_template("blog.html")

@app.route('/contact')

def contact():

    return render_template("contact.html")

@app.route('/gallery')

def gallery():

    return render_template("gallery.html")

@app.route('/room')

def room():

    return render_template("room.html")

if __name__ == "__main__":
    app.run("127.0.0.1", port="8080", debug=True)