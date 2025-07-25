from ninja                       import Router
from ninja_jwt.authentication    import AsyncJWTAuth

from asgiref.sync                import sync_to_async
from typing                      import List

from apps.geo.models.municipio   import Municipio as Model
from apps.geo.schemas.municipio  import FilterSchemaOut

tag     = ['geo']
router  = Router()

@sync_to_async
@router.get("/municipios/{int:estado}/", tags=tag, response=List[FilterSchemaOut])
def filtro(request, estado: int):
    queryset = Model.objects.filter(estado_me_id = estado).all()
    return list(queryset)