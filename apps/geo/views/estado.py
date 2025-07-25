from ninja                      import Router
from ninja_jwt.authentication   import AsyncJWTAuth

from asgiref.sync               import sync_to_async
from typing                     import List

from apps.geo.models.estado     import Estado as Model
from apps.geo.schemas.estado    import FilterSchemaOut

tag     = ['geo']
router  = Router()

@sync_to_async
@router.get("/estados/", tags=tag, response=List[FilterSchemaOut])
def filtro(request):
    queryset = Model.objects.all()
    return list(queryset)