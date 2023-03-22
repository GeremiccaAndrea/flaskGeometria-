from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
def es_cinque():
    return render_template('es_cinque.html')



@app.route('/es_cinque', methods = ["GET"])
def es_cinque2():
    forme = request.args.get("forme") 
    if forme == "cerchio":      
        return render_template("cerchio.html")
    elif forme == "rettangolo":
        return render_template("rettangolo.html")
    elif forme == "pentagono":
        return render_template("pentagono.html")
    else: 
        return render_template("quadrato.html")


@app.route('/areaquadrato' , methods = ['GET'])
def areaquadrato():
  lato = int(request.args.get('lato')) 
  area = lato * lato 
  return render_template("risultato_area_quadrato_es1.html", area = area)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)