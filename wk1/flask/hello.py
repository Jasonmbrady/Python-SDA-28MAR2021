from flask import Flask, render_template
app = Flask(__name__) # __name__ == "__main__"

#  Default Route
@app.route('/') 
def hello_world():
    return render_template('index.html', name = "Ghaida", times = 5)

# Success Route
@app.route('/success')
def success():
    return "success"

#  Say Hi Route
@app.route('/sayhi/<name>')
def sayhi(name):
    return "Hello, " + name


if __name__=="__main__":
    app.run(debug=True)