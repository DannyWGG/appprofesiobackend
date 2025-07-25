from django.db                          import models
from django.contrib.auth.models         import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from simple_history.models              import HistoricalRecords


class UserManager(BaseUserManager):

    def create_user(self, username, email, origen, cedula, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, telefono, estado, municipio, parroquia, password = None):
        user = self.model(
                            username        = username,
                            email           = self.normalize_email(email),
                            origen          = origen,
                            cedula          = cedula,
                            primer_nombre = primer_nombre,
                            segundo_nombre = segundo_nombre,
                            primer_apellido = primer_apellido,
                            segundo_apellido = segundo_apellido,
                            telefono = telefono,
                            estado          = estado,
                            municipio          = municipio,
                            parroquia          = parroquia,
                            )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, origen, cedula, primer_nombre, primer_apellido, telefono, estado, password=None, **extra_fields):
        extra_fields.setdefault('segundo_nombre', '')
        extra_fields.setdefault('segundo_apellido', '')
        extra_fields.setdefault('municipio', '')
        extra_fields.setdefault('parroquia', '')
        
        user = self.create_user(
            username=username,
            email=email,
            origen=origen,
            cedula=cedula,
            primer_nombre=primer_nombre,
            segundo_nombre=extra_fields['segundo_nombre'],
            primer_apellido=primer_apellido,
            segundo_apellido=extra_fields['segundo_apellido'],
            telefono=telefono,
            estado=estado,
            municipio=extra_fields['municipio'],
            parroquia=extra_fields['parroquia'],
            password=password
        )
        
        # Asignar los atributos de superusuario después de crear el usuario
        user.is_superuser = True
        user.is_staff = True
        user.save()
        
        return user

class User(AbstractBaseUser, PermissionsMixin):
    V    =   'V'
    E    =   'E'

    ORIGEN  =   (
                    (V,  'V'),
                    (E,  'E'),
                )

    ESTADOS =   ( 
                    ("AMAZONAS", "AMAZONAS"), 
                    ("ANZOATEGUI", "ANZOATEGUI"), 
                    ("APURE", "APURE"), 
                    ("ARAGUA", "ARAGUA"), 
                    ("BARINAS", "BARINAS"), 
                    ("BOLIVAR", "BOLIVAR"), 
                    ("CARABOBO", "CARABOBO"), 
                    ("COJEDES", "COJEDES"),
                    ("DELTA AMACURO", "DELTA AMACURO"),
                    ("CARACAS", "CARACAS"),
                    ("FALCON", "FALCON"),
                    ("GUARICO", "GUARICO"),
                    ("LA GUAIRA", "LA GUAIRA"),
                    ("LARA", "LARA"),
                    ("MERIDA", "MERIDA"),
                    ("MIRANDA", "MIRANDA"),
                    ("MONAGAS", "MONAGAS"),
                    ("NUEVA ESPARTA", "NUEVA ESPARTA"),
                    ("PORTUGUESA", "PORTUGUESA"),
                    ("SUCRE", "SUCRE"),
                    ("TACHIRA", "TACHIRA"),
                    ("TRUJILLO", "TRUJILLO"),
                    ("YARACUY", "YARACUY"),
                    ("ZULIA", "ZULIA"),
                )

    username                = models.CharField('Usuario',                   max_length =  20,   unique = True,                              )
    email                   = models.EmailField('Correo',                   max_length = 255,   unique = True                               )
    origen                  = models.CharField('Origen',                    max_length =   1,   choices = ORIGEN                            )
    cedula                  = models.IntegerField('Cédula',                                                                                 )
    primer_nombre         = models.CharField('primer_nombre',                   max_length = 255,)
    segundo_nombre = models.CharField('segundo_nombre', max_length=255, blank=True, null=True, default='')
    primer_apellido         = models.CharField('primer_apellido',                   max_length = 255,)
    segundo_apellido = models.CharField('segundo_apellido', max_length=255, blank=True, null=True, default='')
    telefono = models.BigIntegerField('telefono')

    pregunta_01             = models.CharField('Preg. 01',                  max_length = 255,   default = 'INDETERMINADA'                   )
    pregunta_02             = models.CharField('Preg. 02',                  max_length = 255,   default = 'INDETERMINADA'                   )
    pregunta_03             = models.CharField('Preg. 03',                  max_length = 255,   default = 'INDETERMINADA'                   )
    respuesta_01            = models.CharField('Resp. 01',                  max_length = 255,   default = 'INDETERMINADA'                   )
    respuesta_02            = models.CharField('Resp. 02',                  max_length = 255,   default = 'INDETERMINADA'                   )
    respuesta_03            = models.CharField('Resp. 03',                  max_length = 255,   default = 'INDETERMINADA'                   )
    fecha_registro          = models.DateTimeField('Fecha Registro',        auto_now_add = True                                             )
    fecha_actualizacion     = models.DateTimeField('Fecha Actualización',   auto_now = True                                                 )
    estado                  = models.CharField('Estado',                    max_length = 255, blank = True, null = True)
    municipio = models.CharField('municipio', max_length=255, blank=True, null=True, default='')
    parroquia = models.CharField('parroquia', max_length=255, blank=True, null=True, default='')
    is_verified             = models.BooleanField('VERIFICADO',                                  default = True                             )
    is_active               = models.BooleanField('ACTIVO',                                      default = True                             )
    is_staff                = models.BooleanField('STAFF',                                       default = False                            )
    is_superuser            = models.BooleanField('ROOT',                                        default = False                            )
    objects                 = UserManager()
    
    class Meta:
        managed             = True
        db_table            = 'cuenta\".\"usuario'
        verbose_name        = 'Usuario'
        verbose_name_plural = 'Usuarios'
        unique_together     = ('origen','cedula')

    USERNAME_FIELD  = 'username'
    REQUIRED_FIELDS = ['origen','cedula','primer_nombre','primer_apellido','telefono','email','estado']

    def __str__(self):
        return self.username