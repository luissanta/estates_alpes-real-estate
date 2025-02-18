import os

from flask import Flask, render_template, request, url_for, redirect, jsonify, session
from flask_swagger import swagger

from config import Setting

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))

def registrar_handlers():
<<<<<<< HEAD
    import app.moduls.lists.aplication
    import app.moduls.locations.aplication
    #import aeroalpes.modulos.vuelos.aplicacion
=======
    import app.moduls.locations.aplication
    #import app.moduls.lists.aplication
>>>>>>> develop

def importar_modelos_alchemy():
    import app.moduls.lists.infrastructure.dto
    import app.moduls.locations.infrastructure.dto
    

<<<<<<< HEAD
def comenzar_consumidor():
    """
    Este es un código de ejemplo. Aunque esto sea funcional puede ser un poco peligroso tener 
    threads corriendo por si solos. Mi sugerencia es en estos casos usar un verdadero manejador
    de procesos y threads como Celery.
    """

    #import threading
    # import app.modules.lists.infrastructure.co as cliente
    # import aeroalpes.modulos.hoteles.infraestructura.consumidores as hoteles
    # import aeroalpes.modulos.pagos.infraestructura.consumidores as pagos
    # import aeroalpes.modulos.precios_dinamicos.infraestructura.consumidores as precios_dinamicos
    # import aeroalpes.modulos.vehiculos.infraestructura.consumidores as vehiculos
    #import app.moduls.lists.infrastructure.consumers as list_consumer
    import app.moduls.locations.infrastructure.consumers as location_consumer    
    import threading
    # Suscripción a eventos
    # threading.Thread(target=cliente.suscribirse_a_eventos).start()
    # threading.Thread(target=hoteles.suscribirse_a_eventos).start()
    # threading.Thread(target=pagos.suscribirse_a_eventos).start()
    # threading.Thread(target=precios_dinamicos.suscribirse_a_eventos).start()
    # threading.Thread(target=vehiculos.suscribirse_a_eventos).start()
    #threading.Thread(target=list_consumer.suscribirse_a_eventos).start()
    threading.Thread(target=location_consumer.suscribirse_a_eventos).start()
    # # Suscripción a comandos
    # threading.Thread(target=cliente.suscribirse_a_comandos).start()
    # threading.Thread(target=hoteles.suscribirse_a_comandos).start()
    # threading.Thread(target=pagos.suscribirse_a_comandos).start()
    # threading.Thread(target=precios_dinamicos.suscribirse_a_comandos).start()
    # threading.Thread(target=vehiculos.suscribirse_a_comandos).start()
    #threading.Thread(target=location_consumer.suscribirse_a_comandos).start()
=======
def comenzar_consumidor(app):
    import app.moduls.lists.infrastructure.consumers as list_consumer   
    import threading

# Suscripción a eventos
    #threading.Thread(target=list_consumer.suscribirse_a_eventos).start()
>>>>>>> develop

# Suscripción a comandos
    threading.Thread(target=list_consumer.suscribirse_a_comandos_from_response_company).start()
    threading.Thread(target=list_consumer.suscribirse_a_comandos_from_response_rollback_company, args=[app]).start()
    threading.Thread(target=list_consumer.suscribirse_a_comandos_from_response_audit).start()
    threading.Thread(target=list_consumer.suscribirse_a_comandos_from_response_rollback_audit).start()
    threading.Thread(target=list_consumer.suscribirse_a_comandos_from_response_rollback_estate).start()
    threading.Thread(target=list_consumer.suscribirse_a_comandos_from_response_create_estate).start()
    threading.Thread(target=list_consumer.suscribirse_a_comandos_delete, args=[app]).start()
#, args=[app]
def create_app(configuracion={}):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = Setting.DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['TESTING'] = configuracion.get('TESTING')

     # Inicializa la DB
    from app.config.db import init_db
    init_db(app)

    from app.config.db import db

    importar_modelos_alchemy()
    registrar_handlers()

    with app.app_context():
        db.create_all()
        #if not app.config.get('TESTING'):
        comenzar_consumidor(app)

        #from app.moduls.sagas.aplicacion.coordinadores.saga_propiedad import CoordinadorReservas
        #CoordinadorReservas()

     # Importa Blueprints
    from . import list_router

    # Registro de Blueprints
    app.register_blueprint(list_router.bp)

    @app.route("/spec")
    def spec():
        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "My API"
        return jsonify(swag)

    @app.route("/health")
    def health():
        return {"status": "up"}

    return app