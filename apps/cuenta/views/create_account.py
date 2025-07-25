from django.core.exceptions import ValidationError
from django.db import IntegrityError
from ninja import Router
from ninja_jwt.authentication import JWTAuth
from ninja_extra import api_controller, route
from ninja.errors import ValidationError as NinjaValidationError
from ninja_extra.exceptions     import APIException
from typing import Dict, Any

from configuracion.schemes import SucessSchema, ErrorSchema
from apps.cuenta.schemes.token import CreateUserSchema

from ninja_extra.throttling import UserRateThrottle

router = Router()
tag = ['auth']

@api_controller("/auth", tags=tag, permissions=[])  # Ajusta permisos según necesites
class CreateUserController:
    
    @route.post(
        "/create/",
        response={
            201: SucessSchema,
            400: ErrorSchema,
            409: ErrorSchema,
            500: ErrorSchema
        },
        url_name="user-create",
        summary="Registrar nuevo usuario",
        description="Crea un nuevo usuario con roles de Afiliado o Cliente"
    )
    def create_user(self, user_data: CreateUserSchema) -> Dict[str, Any]:

        try:
            # Validación y creación del usuario
            user = user_data.create()
            
            # Respuesta exitosa
            return 201, {
                "message": "Usuario registrado exitosamente",
                "details": {
                    "user_id": user.id,
                    "username": user.username,
                    "roles": [role.name for role in user.groups.all()]
                }
            }
            
        except NinjaValidationError as e:
            # Captura errores de validación de Pydantic
            return 400, {
                "message": "Error de validación",
                "errors": e.errors()
            }
            
        except IntegrityError as e:
            # Captura errores de unicidad (username/email/cedula duplicados)
            return 409, {
                "message": "Conflicto de datos",
                "details": str(e)
            }
            
        except ValidationError as e:
            # Captura errores de validación de Django
            return 400, {
                "message": "Error en los datos proporcionados",
                "errors": e.message_dict if hasattr(e, 'message_dict') else str(e)
            }
            
        except APIException as e:
            # Captura excepciones específicas de tu lógica
            return 400, {
                "message": str(e)
            }
            
        except Exception as e:
            # Captura cualquier otro error inesperado
            return 500, {
                "message": "Error interno del servidor",
                "details": str(e)
            }