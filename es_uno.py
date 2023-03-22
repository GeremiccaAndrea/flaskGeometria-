from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def es_uno():
    return render_template('es_uno.html')


@app.route('/areaquadrato' , methods = ['GET'])
def areaquadrato():
  lato = int(request.args.get('lato')) 
  area = lato * lato 
  return render_template("risultato_area_quadrato_es1.html", area = area)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)