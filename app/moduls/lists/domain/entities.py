"""Entidades del dominio de lists

En este archivo usted encontrará las entidades del dominio de lists
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
import uuid
from app.moduls.lists.domain.events import ReservaCreada
import app.moduls.lists.domain.value_objects as ov
from app.moduls.lists.infrastructure.schema.v1.commands import  ComandoCrearReservaPayload
from app.seedwork.domain.entities import Entity, RootAggregation

@dataclass
class Companies(Entity):
    _id: str = field(default_factory=str)
    company_name: str = field(default_factory=str)
    location: str = field(default_factory=str)
    typeCompany: str = field(default_factory=str)

@dataclass
class GeoLocation(Entity): 
    _id: str = field(default_factory=str)   
    lat: str = field(default_factory=str)
    lon: str = field(default_factory=str)

@dataclass
class Estate(Entity):    
    _id: str = field(default_factory=str)
    code: str = field(default_factory=str)
    name: str = field(default_factory=str)
    geo_locations: list[GeoLocation] = field(default_factory=list[GeoLocation])
    companies: list[Companies] = field(default_factory=list[Companies])
    
    # createdAt: str = field(default_factory=str)
    # updatedAt: str = field(default_factory=str)

@dataclass
class List_estates(RootAggregation):
    _id: str = field(default_factory=str)
    id: str = field(hash=True, default=None)
    estates: list[Estate] = field(default_factory=list)
    created_at: datetime = field(default=datetime.now())
    updated_at: datetime = field(default=datetime.now())
    data: str = field(default_factory=str)
       

    def create_estate(self, estateslist: List_estates):
        estates = estateslist
<<<<<<< HEAD
        for estate in estateslist.estates:
            #elf.updatedAt = None #datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
            self.add_events(ReservaCreada(id=estate.id,id_reserva=estate.id, id_cliente=estate.code, estado=estate.name, fecha_creacion=datetime.now()))

        
=======
        cmd = ComandoCrearReservaPayload()
        cmd.data  = estateslist.data
        cmd.id = estateslist.id
        for estate in estates.estates:
            for geo_locations in estate.geo_locations:
                cmd.locations.append({"estate_id": estate.id, "code": geo_locations.lat, "name": geo_locations.lon})
                self.add_events(cmd)    

            # for companies in estate.companies:
                # example_data = str({
                #     "id": str(uuid.uuid4),
                #     "name": companies.company_name,
                #     "location": companies.location,
                #     "typeCompany": companies.typeCompany
                # })
                #TODO MB payload = CommandCreateCompanyJson(
                #      data=example_data    
                # )
                # self.add_events(payload)

        #Datos Auditoria
        # example_data = str({
        #     "id": str(uuid.uuid4),
        #     "code": "code",
        #     "score": 95, #float  -- Random de 1 a 100
        #     "approved_audit": "code" #bool
        # })
        # cmd = CommandCreateAuditJson(
        #     data = example_data
        # )
        #TODO self.add_events(cmd)
>>>>>>> develop
