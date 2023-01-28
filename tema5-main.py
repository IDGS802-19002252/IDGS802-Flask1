from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  titulo='Hola Hola'
  lista=['Pedro', 'que', 'gusto', 'de', 'verte']
  return render_template('index.html', titulo=titulo, lista=lista)

if __name__ == '__main__':
  app.run(debug=True, port=8000)