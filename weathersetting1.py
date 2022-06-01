from flask import Flask, render_template ,request,url_for


app = Flask(__name__)

@app.route ("/")
@app.route("/home")

def home():
    return render_template("index.html")


@app.route("/result", methods = ['POST', "GET"])
def result():
    output = request.form.to_dict()
    print(output)
    area = output["area"]

    return render_template('index.html', area = area)

if __name__ == '__main__':
    app.run(debug=True)