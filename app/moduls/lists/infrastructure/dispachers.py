import json
import pulsar

from app.moduls.lists.infrastructure.schema.v1.events import EventoDominioReservaCreada, EventoReservaCreada, ReservaCreadaPayload
from app.moduls.lists.infrastructure.schema.v1.commands import ComandoCrearReserva, ComandoCrearReservaPayload
from app.seedwork.infrastructure import utils
from pulsar.schema import JsonSchema, Record
import datetime
import logging

# Enable Pulsar client logging
logging.basicConfig(level=logging.DEBUG)
epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class DespachadorDominio:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        print("1ENTROOOOOOOOOOOOOOOOOOOOOOOOOOOO")
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoDominioReservaCreada))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del evento
        payload = ReservaCreadaPayload(
            id_reserva=str(evento.id_reserva), 
            id_cliente=str(evento.id_cliente), 
            estado=str(evento.estado), 
            fecha_creacion=int(unix_time_millis(evento.fecha_creacion))
        )
        #evento_integracion = EventoReservaCreada(data=payload)
        evento_dominio = EventoDominioReservaCreada(data=payload)
        #self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoReservaCreada))
        print("ENTROOOOOOOOOOOOOOOOOOOOOOOOOOOO")
        print(topico)

        self._publicar_mensaje(evento_dominio, topico, AvroSchema(EventoDominioReservaCreada))
        

    def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        payload = ComandoCrearReservaPayload(
            id_usuario=str(comando.id_usuario)
            # agregar itinerarios
        )
        comando_integracion = ComandoCrearReserva(data=payload)
        print("NENTROOOOOOOOOOOOOOOOOOOOOOOOOOOO")
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearReserva))

class Despachador:
    def _publicar_mensaje(self, mensaje, topico):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico)
        serialized_data = json.dumps(mensaje.data).encode('utf-8')       
        publicador.send(serialized_data)
        publicador.close()

    def publicar_evento(self, evento, topico):
        payload = ReservaCreadaPayload(
            id_reserva=str(evento.id_reserva), 
            id_cliente=str(evento.id_cliente), 
            estado=str(evento.estado), 
            fecha_creacion=int(unix_time_millis(evento.fecha_creacion))
        )
        evento_integracion = ComandoCrearReserva(data=payload)
        #self._publicar_mensaje(evento_integracion, topico, schema= AvroSchema(ComandoCrearReserva))

    def publicar_comando(self, comando, topico):
        self._publicar_mensaje(comando, topico)
