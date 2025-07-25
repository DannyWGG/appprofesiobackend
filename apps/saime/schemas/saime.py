#from ninja_schema   import Schema
from ninja          import FilterSchema, Field, Schema
from typing         import Optional
from datetime import date


class SaimeSchemaOut(Schema):
    origen: 				str
    cedula: 				int	
    #pais_origen: 			str
    #nacionalidad: 			str
    primer_nombre: 			str
    segundo_nombre:         Optional[str] = None
    primer_apellido: 		str
    segundo_apellido:       Optional[str] = None
    fecha_nacimiento:       date
    sexo: 					str
    #fecha_registro: 		str
    #fecha_ult_actualizacion: str 
    