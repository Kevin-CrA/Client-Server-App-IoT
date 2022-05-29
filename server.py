from flask import Flask, request

app = Flask('__main__')


"""
Codigo de prueba, ta feo --suponer que viene de la DB
"""
device={
    "code":123444,
    "descrip":"Temp. sensor",
    "value":67
}


@app.route('/devices',methods=['GET']) #SE EJECUTA METODO DESPUES DE LA RUTA DE /
def go_home():
    print(device)
    return device #'Hello world'

#Save an user
@app.route('/users', methods=['POST'])
def save():
    user= request.json
    print(user)
    return user
    
#Save a device
@app.route('/devices',methods=['POST'])
def save_device():
    device=request.json
    print(device)
    return device, 201


if __name__ == '__main__':
    app.run(debug=True, port=5000,host='0.0.0.0')

    #localhost:5000/users <----endpoint