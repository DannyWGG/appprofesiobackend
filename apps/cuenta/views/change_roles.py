from ninja                      import Router
from ninja_jwt.authentication   import AsyncJWTAuth


from configuracion.schemes      import SucessSchema, ErrorSchema
from apps.cuenta.models         import User as Model
from apps.cuenta.schemes.token  import UpdateRolesSchema

from django.contrib.auth.models import Group

router = Router()
tag = ['auth']

@router.post('/update-roles/', tags=tag, response={200: dict, 404: dict, 400: dict})
def update_roles(request, payload: UpdateRolesSchema):
    try:
        # Obtener usuario y validar existencia
        user = Model.objects.get(id=payload.user_id)
        
        # Limpiar roles actuales antes de asignar los nuevos
        user.groups.clear()
        
        # Asignar nuevos roles con validación
        for role in payload.roles:
            group, created = Group.objects.get_or_create(name=role.value)
            user.groups.add(group)
        
        return 200, {
            "status": "success",
            "message": "Roles actualizados correctamente",
            "new_roles": [role.value for role in payload.roles]
        }
    
    except Model.DoesNotExist:
        return 404, {
            "status": "error",
            "message": "Usuario no encontrado"
        }
    
    except Exception as e:
        return 400, {
            "status": "error",
            "message": str(e)
        }