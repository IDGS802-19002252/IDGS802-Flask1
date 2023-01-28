from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return 'buenas buenas buenas'

@app.route('/user/<string:user>')
def user(user):
  return f'<h1>{user}</h1>'

@app.route('/number/<int:n>')
def number(n):
  return f'<h2>{n}</h2>'

@app.route('/user/<string:user>/<int:n>')
def username(user, n):
  return f'<h1>{user} -> {n}</h1>'

@app.route('/suma/<float:n1>/<float:n2>')
def suma(n1, n2):
  return f'<h1>{n1} + {n2} = {n1+n2}</h1>'

@app.route('/default')
@app.route('/default/<string:n>')
def sum(n='nada'):
  return f'<h1>Valor de n -> {n}</h1>'

if __name__ == '__main__':
  app.run(debug=True, port=8000)