from . import app, db
from .models import Medico, Paciente, Consultorio, Cita
from flask import render_template, request

#crear ruta para ver los medicos 
@app.route("/medicos")
def get_all_medicos():
        medicos = Medico.query.all()
        return render_template("medicos.html" , medicos=medicos)

@app.route("/pacientes")
def get_all_pacientes():
        pacientes = Paciente.query.all()
        return render_template("pacientes.html" , pacientes=pacientes)

@app.route("/consultorios")
def get_all_consultorios():
        consultorios = Consultorio.query.all()
        return render_template("consultorios.html" , consultorios=consultorios)

@app.route("/citas")
def get_all_citas():
        citas = Cita.query.all()
        return render_template("citas.html" , citas=citas)

##crear ruta traer el medico por id (get)
@app.route("/medicos/<int:id>")
def get_all_medicos_by_id(id):
        medico= Medico.query.get(id)
        return render_template("medico.html", 
                                med = medico )
@app.route("/pacientes/<int:id>")
def get_all_pacientes_by_id(id):
        paciente= Paciente.query.get(id)
        return render_template("paciente.html", 
                                pac = paciente )
@app.route("/consultorios/<int:id>")
def get_all_consultorios_by_id(id):
        consultorio= Consultorio.query.get(id)
        return render_template("consultorio.html", 
                                con = consultorio )
#crear ruta para crear nuevo medico
@app.route("/medicos/create" , methods = [ "GET" , "POST"] )
def create_medico():
        #######
        #mostrar el formulario: metodo GET
        #######
        if( request.method == 'GET'):
                #usuario ingreso con navegador con http://localhost:5000/medicos/create
                especialidades = [
                        "Cardiologia",
                        "Pediatria",
                        "Oncologia"
                ]        
                return render_template("medico_form.html" , 
                                especialidades = especialidades ) 
        elif(request.method == 'POST'):
                #cuando se presiona "guardar"
                #crear un objeto de tipo medico
                new_medico = Medico(nombre = request.form['nombre'],apellido = request.form['apellido'],tipo_identificacion = request.form['ti'],numero_identificacion = request.form['ni'],registro_medico = request.form['rm'],especialidad = request.form['es'])

                #añadir a la sesion sqlalchemy
                db.session.add(new_medico)
                db.session.commit()
                return 'medico registrado'

        ###
        ## Cuando el usuario presiona el boton de guardar 
        ### los datos del formulario viajan al servidor 
        ## utilizando el metodo POST