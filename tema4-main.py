from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
  return 'buenas buenas buenas'

@app.route('/operasBas', methods=['GET', 'POST'])
def operasBas():
  if request.method == 'POST':
    num1 = request.form.get('num1')
    num2 = request.form.get('num2')
    op = request.form.get('operacion')
    match(op):
      case 'suma':
        return f'<h2>La suma es: {str(int(num1)+int(num2))}</h2>'
      case 'resta':
        return f'<h2>La resta es: {str(int(num1)-int(num2))}</h2>'
      case 'multi':
        return f'<h2>La multiplicación es: {str(int(num1)*int(num2))}</h2>'
      case 'div':
        return f'<h2>La división es: {str(int(num1)/int(num2))}</h2>'
  else:
    return '''
    <style>
     form {
      width: 30%;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: .5rem;
     }

     input {
      padding: .5rem 0;
     }
    </style>
    <form action='/operasBas' method='POST'>
    <label>Operaciones</label>
    <div>
    <label>
      <input type='radio' name='operacion' value='suma'>
      Suma
    </label>
    <label>
    <input type='radio' name='operacion' value='resta'>
    Resta
    </label>
    <label>
    <input type='radio' name='operacion' value='multi'>
    Multiplicación
    </label>
    <label>
    <input type='radio' name='operacion' value='div'>
    División
    </label>
    </div>
    <label>N1:</label>
    <input type='text' name='num1' /> <br><br>
    <label>N2:</label>
    <input type='text' name='num2' /> <br><br>
    <input type='submit' value='Calcular' /> <br><br>
    </form>
    '''
if __name__ == '__main__':
  app.run(debug=True, port=8000)