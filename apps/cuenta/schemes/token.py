from ninja_jwt.schema           import TokenObtainPairInputSchema
from ninja_jwt.tokens           import RefreshToken
from ninja_schema               import ModelSchema, Schema, model_validator
from ninja                      import Schema, Field
from ninja_extra.exceptions     import APIException
from pydantic                   import EmailStr
from enum import Enum

from typing                     import Type, Dict, List
from django.contrib.auth.models import Group
from apps.cuenta.models         import User


# Excepción personalizada para conflictos 409
class ConflictException(APIException):
    status_code = 409
    default_detail = "Recurso ya existe (conflicto)"


class GroupSchema(ModelSchema):
    class Config:
        model = Group
        include = ("name",)


class UserSchema(ModelSchema):
    groups: List[GroupSchema]
    origen: str = Field(alias="origen")
    estado: str = Field(alias="estado")

    class Config:
        model = User
        include = (
            "id",
            "username",
            "origen",
            "cedula",
            "primer_nombre",
            "segundo_nombre",
            "primer_apellido",
            "segundo_apellido",
            "telefono",
            "estado",
            "municipio",
            "parroquia",
            "email",
            "pregunta_01",
            "pregunta_02",
            "pregunta_03",
            "respuesta_01",
            "respuesta_02",
            "respuesta_03",
        )


class MyTokenObtainPairOutSchema(Schema):
    refresh: str
    access: str
    user: UserSchema


class MyTokenObtainPairSchema(TokenObtainPairInputSchema):
    @classmethod
    def get_response_schema(cls) -> Type[Schema]:
        return MyTokenObtainPairOutSchema

    @classmethod
    def get_token(cls, user) -> Dict:
        values = {}
        refresh = RefreshToken.for_user(user)
        values["refresh"] = str(refresh)
        values["access"] = str(refresh.access_token)
        values.update(user=UserSchema.from_orm(user))
        return values


class UserRole(str, Enum):
    AFILIADO = "Afiliado"
    CLIENTE = "Cliente"

    @classmethod
    def get_values(cls):
        return [role.value for role in cls]


class CreateUserSchema(ModelSchema):
    origen: str = Field(..., alias="origen", max_length=1)
    roles: List[UserRole] = Field(
        ...,
        description=f"Roles asignables: {UserRole.get_values()}"
    )
    password: str = Field(..., min_length=8)

    class Config:
        model = User
        include = [
            "username",
            "origen",
            "cedula",
            "primer_nombre",
            "segundo_nombre",
            "primer_apellido",
            "segundo_apellido",
            "telefono",
            "estado",
            "municipio",
            "parroquia",
            "email",
            "password",
        ]

    @model_validator("estado")
    def estado_valido(cls, v):
        # Si viene un Enum, obtenemos su valor
        if hasattr(v, "value"):
            v_value = v.value
        else:
            v_value = v
        print(f"Mi estado: {v_value}")
        
        valid_estados = [choice[0] for choice in User.ESTADOS]
        if v_value not in valid_estados:
            raise APIException(f"Estado: Debe ser uno de {valid_estados}")
        return v_value

    @model_validator("username")
    def user_null(cls, value_data):
        if value_data == "":
            raise APIException("Usuario: El nombre de usuario no puede estar vacío")
        return value_data

    @model_validator("email")
    def email_null(cls, value_data):
        if value_data == "":
            raise APIException("Correo: El correo no puede estar vacío")
        return value_data

    @model_validator("origen")
    def origen_null(cls, value_data):
        if value_data == "":
            raise APIException("Origen: El origen no puede estar vacío")
        return value_data

    @model_validator("cedula")
    def cedula_null(cls, value_data):
        if value_data == "":
            raise APIException("Cédula: El número de cédula no puede estar vacío")
        return value_data

    @model_validator("primer_nombre")
    def primer_nopmbre_null(cls, value_data):
        if value_data == "":
            raise APIException("Nombre: El nombre no puede estar vacío")
        return value_data
    
    @model_validator("primer_apellido")
    def primer_apellido_null(cls, value_data):
        if value_data == "":
            raise APIException("Apellido: El apellido no puede estar vacío")
        return value_data
    
    @model_validator("telefono")
    def telefono_null(cls, value_data):
        if value_data == "":
            raise APIException("Telefono: El telefono no puede estar vacío")
        return value_data

    @model_validator("estado")
    def estado_null(cls, value_data):
        if value_data == "":
            raise APIException("Estado: El estado no puede estar vacío")
        return value_data

    @model_validator("password")
    def password_null(cls, value_data):
        if value_data == "":
            raise APIException("Clave: La clave no puede estar vacía")
        return value_data

    @model_validator("username")
    def unique_username(cls, value_data):
        if User.objects.filter(username=value_data).exists():
            raise ConflictException("Usuario: Este nombre de usuario ya está registrado")
        return value_data

    @model_validator("email")
    def unique_email(cls, value_data):
        if User.objects.filter(email__iexact=value_data).exists():
            raise ConflictException("Correo: Este correo ya está registrado")
        return value_data

    @model_validator("origen")
    def origen_validate(cls, value_data):
        if value_data == 'V' or value_data == 'E':
            return value_data
        raise APIException("Origen: Las opciones válidas son V o E")

    @model_validator("cedula")
    def unique_cedula(cls, value_data):
        if User.objects.filter(origen='V', cedula=value_data).exists() or \
           User.objects.filter(origen='E', cedula=value_data).exists():
            raise ConflictException("Cédula: Esta cédula ya está registrada")
        return value_data

    def create(self) -> User:
        user_data = self.dict(exclude={"roles"})

        # Crear el usuario
        user = User.objects.create_user(**user_data)

        # Asignar roles con validación
        for role in self.roles:
            group, created = Group.objects.get_or_create(name=role.value)
            if created:
                group.save()  # Guarda el grupo si es nuevo

            # Validar que no sea administrador
            if group.name.lower() == "administrador":
                user.delete()  # Eliminar usuario si se intenta asignar admin
                raise APIException("No se puede asignar el rol de administrador")

            user.groups.add(group)

        return user


class UserResponseSchema(Schema):
    id: int
    username: str
    email: str
    estado: str
    roles: List[str] = Field(..., alias="groups")

    @staticmethod
    def resolve_roles(obj):
        return [group.name for group in obj.groups.all()]

class UpdateRolesSchema(Schema):
    user_id: int = Field(..., description="ID del usuario a modificar")
    roles: List[UserRole] = Field(
        ...,
        description=f"Lista de roles a asignar. Opciones: {UserRole.get_values()}"
    )

class ChangePasswordSchema(Schema):
    user_id: int
    old_password: str
    new_password: str


class ChangeEmailSchema(Schema):
    email: EmailStr

    class Config:
        model = User
        include = ("email",)

    @model_validator("email")
    def emty_email(cls, value_data):
        if value_data == "":
            raise APIException("El correo es obligatorio")
        return value_data

    @model_validator("email")
    def unique_email(cls, value_data):
        if User.objects.filter(email__iexact=value_data).exists():
            raise ConflictException("Este correo ya está registrado")
        return value_data


class ChangeQASchema(ModelSchema):
    class Config:
        model = User
        include = (
            "pregunta_01",
            "pregunta_02",
            "pregunta_03",
            "respuesta_01",
            "respuesta_02",
            "respuesta_03",
        )

    @model_validator("pregunta_01")
    def pregunta_01_vacia(cls, value_data):
        if value_data == "":
            raise APIException("La Pregunta 01 no puede estar vacía")
        return value_data

    @model_validator("pregunta_02")
    def pregunta_02_vacia(cls, value_data):
        if value_data == "":
            raise APIException("La Pregunta 02 no puede estar vacía")
        return value_data

    @model_validator("pregunta_03")
    def pregunta_03_vacia(cls, value_data):
        if value_data == "":
            raise APIException("La Pregunta 03 no puede estar vacía")
        return value_data

    @model_validator("respuesta_01")
    def respuesta_01_vacia(cls, value_data):
        if value_data == "":
            raise APIException("La Respuesta 01 no puede estar vacía")
        return value_data

    @model_validator("respuesta_02")
    def respuesta_02_vacia(cls, value_data):
        if value_data == "":
            raise APIException("La Respuesta 02 no puede estar vacía")
        return value_data

    @model_validator("respuesta_03")
    def respuesta_03_vacia(cls, value_data):
        if value_data == "":
            raise APIException("La Respuesta 03 no puede estar vacía")
        return value_data
