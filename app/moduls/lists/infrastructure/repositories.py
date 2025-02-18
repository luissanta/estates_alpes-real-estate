""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de lists
"""

from app.config.db import db
from app.moduls.lists.domain import factories
from seeders.logapp import agregar_mensaje
from .dto import List_estates as List_estatesDTO
from ..domain.entities import List_estates
from ..domain.repositories import ListRepository
from ..domain.factories import ListFactory
from ..infrastructure.mappers import MapeadorEstate


class EstateRepositoryPostgres(ListRepository):

    

    def __init__(self):
        self._estates_factory: ListFactory = ListFactory()
        self.error_msg = "Error: "

    @property
    def estates_factory(self):
        return self._estates_factory

    def get_by_id(self, entity_id: int) -> List_estates:        
        list_estate_dto = db.session.query(List_estatesDTO).filter_by(id=str(entity_id)).one()
        try:    
            estate_list_entity = self.estates_factory.create_object(list_estate_dto, MapeadorEstate())      
            agregar_mensaje("get_by_id List_estatesDTO ok : "+str(estate_list_entity.id))        
        except Exception as e:
            agregar_mensaje("get_by_id error List_estatesDTO "+str(e))
            print(self.error_msg, e)
        
        return estate_list_entity

    def get_all(self) -> list[List_estates]:
        estate_list_entity = None
        try:    
            list_estate_dto = db.session.query(List_estatesDTO).all()
            estate_list_entity = self.estates_factory.create_object(list_estate_dto, MapeadorEstate())    
            agregar_mensaje("get_all List_estatesDTO ok : "+str(estate_list_entity.id))         
        except Exception as e:
            agregar_mensaje("get_all error List_estatesDTO "+str(e))
            print(self.error_msg, e)

        return estate_list_entity

    def create(self, entity: List_estates):
        try:
            listesates_dto = self.estates_factory.create_object(entity, MapeadorEstate())         
            db.session.add(listesates_dto)
            agregar_mensaje("create List_estatesDTO ok : "+str(listesates_dto.id))
        except Exception as e:
            agregar_mensaje("create error List_estatesDTO "+str(e))
            print(self.error_msg, e)

    def update(self, entity_id: int, entity: List_estates):
        raise NotImplementedError

    def delete(self, entity_id: int):
        try:
            listesates_dto = None
            if(entity_id.id == -1):
                listesates_dto = db.session.query(List_estatesDTO).order_by(List_estatesDTO.id.desc()).first()
            else:
                listesates_dto = db.session.query(List_estatesDTO).filter_by(id=entity_id.id).one()
            db.session.delete(listesates_dto)
            agregar_mensaje("delete List_estatesDTO ok : "+str(entity_id.id))
        except Exception as e:
            agregar_mensaje("delete error List_estatesDTO "+str(e))
            print(self.error_msg, e)
