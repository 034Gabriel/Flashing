from flask import Flask, flash

app = Flask('app')

@app.route('/')
def hello_world():
  return '<h1>Hello, World!</h1>'

@app.route('/flashing')
def flashing():
  flash('Sucesso', 'success')
  return '<p>Flashing</p>'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)