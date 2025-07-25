from ninja                      import Router
from ninja.security             import HttpBearer
from ninja_extra.pagination     import (paginate, PageNumberPaginationExtra, PaginatedResponseSchema)
from ninja_extra.ordering       import ordering, Ordering
from ninja_extra.searching      import searching, Searching
from ninja_jwt.authentication   import JWTAuth
from configuracion.schemes      import ErrorSchema as SchemaError, SucessSchema
from asgiref.sync                   import sync_to_async

        
from apps.saime.models.saime   import Saime   as Model
from apps.saime.schemas.saime  import SaimeSchemaOut  as SchemaOut
tag = ['saime']

router = Router()


@sync_to_async
@router.get('/persona/{str:origen}/{int:cedula}/', tags=tag, response = {200: SchemaOut, 400: dict, 401: dict})
def filtro(request, origen: str, cedula: int):
    '''
    data = Model.objects.filter(origen = origen, cedula = cedula).first()
    #return list(data)
    return data
    '''
    try:
        data = Model.objects.get(origen=origen, cedula=cedula)
        return data
    except Model.DoesNotExist:
        return 404, {"message": "No hay datos"}