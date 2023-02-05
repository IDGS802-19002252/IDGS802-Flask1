from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/cinepolis', methods=['GET'])
def index():
  return render_template('cinepolis.html')

@app.route('/calcular', methods=['POST'])
def calcular():
  nombre = request.form.get('nombre')
  compradores = int(request.form['compradores'])
  cineco = request.form.get('cineco')
  boletas = int(request.form['boletas'])

  suma = 0
  total = 0
  descuento = 0
  excedeLimite = False

  if((boletas / compradores) > 7):
    excedeLimite = True
  
  if(boletas > 2 and boletas <= 5):
    descuento += .10
  elif(boletas > 5):
    descuento += .15

  if(cineco == 'si'):
    descuento += .10

  suma = compradores * (boletas * 12000)
  total = suma - (suma * descuento)

  return {
    'limite': excedeLimite,
    'total': total
    }

if __name__ == '__main__':
  app.run(debug=True, port=8000)