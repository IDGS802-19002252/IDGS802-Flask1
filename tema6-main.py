from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/operasbas', methods=['GET'])
def operasBas():
  return render_template('operasbas.html')

@app.route('/resultado', methods=['POST'])
def resultado():
  n1 = request.form.get('txtNum1')
  n2 = request.form.get('txtNum2')
  multi = int(n1) * int(n2)
  return render_template('resultado.html', multi = multi)


if __name__ == '__main__':
  app.run(debug=True, port=8000)