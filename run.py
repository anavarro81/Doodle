from flask import Flask, render_template, flash, request

app = Flask(__name__)
app.secret_key = "xxxx"

# Se crea una lista para guardar las fechas. 
fechas = []

@app.route('/', methods=['GET', 'POST'])
def index():    
    
    if request.method == "POST":
       fecha  = request.form.get('fecha')       
       fechas.append(fecha)       
       return render_template('index.html', fechas=fechas) 
    else:
        fecha  = ""
        return render_template('index.html', fechas=fechas)
    



@app.route('/resultado', methods=["POST"])
def resultado():    
    
    # nombre = str(request.form['nombre'])
    # fecha  = request.form['fecha']
    # # confirmar_fecha = str(request.form['confirma-fecha'])   
    # confirmar_fecha = request.form['confirma-fecha']

    nombre = request.form.get('nombre')
    fecha  = request.form.get('fecha')
    confirmar_fecha = request.form.get('confirmar_fecha')

    print (f'confirmar_fecha= {confirmar_fecha}')

    # if confirmar_fecha is None:        
    #     confirmar_fecha = 'No'
    


    return render_template('resultado.html', nombre=nombre, fecha=fecha, confirmar=confirmar_fecha)
    # return render_template('resultado.html', nombre=nombre)


if __name__ == '__main__':
    app.run(debug=True)