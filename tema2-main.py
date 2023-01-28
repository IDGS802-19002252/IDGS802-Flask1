from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return 'buenas buenas buenas'

@app.route('/juan')
def juan():
  return '<h1>Juan</h1>'

if __name__ == '__main__':
  app.run(debug=True, port=8000)