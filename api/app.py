#https://www.youtube.com/watch?v=riijt-xcqYI new forma de hacer Apirest

from flask import Flask , jsonify, request
from Productos import products
#from name file and  import array or property
app = Flask(__name__)

#Generating route init
@app.route('/')
def home():
    return jsonify({"name":'Hola mundo'})

#generacion de rutas
@app.route('/product')
def product():
    return jsonify(products , "Mensaje","List products ready")


#Route the select product
@app.route('/product/<string:name>')
def getProductosya(name):
    #Array drive for
    GlobalProducts =[products for products in products if products['name'] == name]
   
    #Validamos la longitud el array que estamos validando
    if( len(GlobalProducts) > 0 ):
        return jsonify({"producto": GlobalProducts[0]})
    return jsonify({"mensaje":"Product no encontrado"})

#Route Post
@app.route("/product" , methods=['POST'])
def addproducts():
    new_Product ={
        "name": request.json['name'],
        "price":request.json['price'],
        "quantity":request.json['quantity']
    }
    #add new product
    products.append(new_Product)
    return jsonify({"mensaje":" add correct ", "producto":products})

#update Products 
@app.route('/product/<string:name>' , methods=['PUT'])
def editProducts(name):
    GlobalProducts1 = [products for products in products if products['name'] == name]
    if(len(GlobalProducts1) > 0 ):
        GlobalProducts1[0]['name'] = request.json['name']
        GlobalProducts1[0]['price'] = request.json['price']
        GlobalProducts1[0]['quantity'] = request.json['quantity']
        return jsonify({"messaje":"product update", "product":GlobalProducts1    })
   
    return jsonify({"messaje":"product  no encontrado"   })


#Route delete product
@app.route('/product/<string:name>', methods=['DELETE'])
def deleteProduct(name):
    GlobalProducts2 = [products for products in products if products['name'] == name]
    if (len(GlobalProducts2) > 0 ):
        products.remove(GlobalProducts2[0])
        return jsonify({"mensaje":"Producto Eliminado",
                        "products":products})
        
    return jsonify({"mensaje":"Producto Eliminado"})
    
    
    
    
    
    
    
if __name__ == '__main__':
    app.run(debug = True , port=4000)