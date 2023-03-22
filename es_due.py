from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def es_uno():
    return render_template('es_uno.html')


@app.route('/areaquadratopost' , methods = ['POST'])
def areaquadratopost():
  lato = int(request.form['lato']) 
  area = lato * lato 
  return render_template("es_2.html", area = area)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3246, debug=True)