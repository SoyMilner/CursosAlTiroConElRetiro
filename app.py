from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/episodio1')
def episodio1():
    return render_template('episodio1.html')

@app.route('/episodio2')
def episodio2():
    return render_template('episodio2.html')

if __name__ == '__main__':
    app.run(debug=True)
