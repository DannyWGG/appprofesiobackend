from ninja                       import Router
from ninja_jwt.authentication    import AsyncJWTAuth

from asgiref.sync                import sync_to_async
from typing                      import List

from apps.geo.models.parroquia   import Parroquia as Model
from apps.geo.schemas.parroquia  import FilterSchemaOut

tag     = ['geo']
router  = Router()

@sync_to_async
@router.get("/parroquias/{int:municipio}/", tags=tag, response=List[FilterSchemaOut])
def filtro(request, municipio: int):
    queryset = Model.objects.filter(municipio_me_id = municipio).all()
    return list(queryset)