from flask import Flask, render_template, make_response
from script import chatAZpross
from flask.globals import request

#Flask
app = Flask(__name__)
#pagina 1

#route -> caminho do site

#template

# função -> oq exibir
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/chat", methods=["POST"])
def chatAZ():
        prompt = request.form["valor"]
        response = chatAZpross(prompt)
        return render_template("home.html", resposta=response)

#site no ar
if __name__ == "__main__":
    app.run(debug=True)