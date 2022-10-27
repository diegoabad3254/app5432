from flask import Flask, jsonify	
from articulos import articulos

app = Flask(__name__) 

@app.route('/api')
def api():
    return jsonify({"message":"Hola Mundo!"})


@app.route('/articulos')
def getArticulos():
	    return jsonify({"articulos":articulos, "message":"Listado de articulos"})
 
 
@app.route('/articulos/<string:nom_articulo>')
def getArticulo(nom_articulo):
	encontrado = [articulo for articulo in articulos if articulo['nombre'] == nom_articulo] 
	if (len(encontrado) > 0):
		return jsonify({"articulo": encontrado[0]})
	return jsonify({"message":"Articulo no encontrado"})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=443, ssl_context=('micertificado.pem', 'llaveprivada.pem') )