from pathlib        import Path
from datetime       import timedelta
from decouple       import config, Csv
import os

import logging.config

from urllib.parse import urlparse, parse_qsl
from dotenv import load_dotenv

from import_export.formats.base_formats import XLSX

EXPORT_FORMATS          =   [XLSX]

BASE_DIR                =   Path(__file__).resolve().parent.parent
SECRET_KEY              =   config('SECRET_KEY')
DEBUG                   =   config('DEBUG')
ALLOWED_HOSTS           =   config('ALLOWED_HOSTS', cast=Csv())

BASE_APPS               =   [
                                'django.contrib.admin',
                                'django.contrib.auth',
                                'django.contrib.contenttypes',
                                'django.contrib.sessions',
                                'django.contrib.messages',
                                'django.contrib.staticfiles',
                            ]

LOCAL_APPS              =   [
                                'apps.cuenta',
                                'apps.frontend',
                                'apps.geo',
                                'apps.saime'
                            ]

THIRD_APPS              =   [
                                'corsheaders',
                                'ninja_extra',
                                'ninja_jwt',
                                'ninja_jwt.token_blacklist',
                                'django_rest_passwordreset',
                                'import_export',
                                'maintenance_mode',
                                'simple_history',
                            ]

INSTALLED_APPS          = BASE_APPS + LOCAL_APPS + THIRD_APPS


MIDDLEWARE              =   [
                                'django.middleware.security.SecurityMiddleware',
                                'django.contrib.sessions.middleware.SessionMiddleware',
                                # Incluido
                                "corsheaders.middleware.CorsMiddleware",
                                'django.middleware.common.CommonMiddleware',
                                'django.middleware.csrf.CsrfViewMiddleware',
                                'django.contrib.auth.middleware.AuthenticationMiddleware',
                                'django.contrib.messages.middleware.MessageMiddleware',
                                'django.middleware.clickjacking.XFrameOptionsMiddleware',
                                # Incluido
                                'maintenance_mode.middleware.MaintenanceModeMiddleware',
                                'simple_history.middleware.HistoryRequestMiddleware',
                            ]

ROOT_URLCONF            =   'configuracion.urls'

TEMPLATES               =   [
                                {
                                    'BACKEND'   :   'django.template.backends.django.DjangoTemplates',
                                    'DIRS'      :   [os.path.join(BASE_DIR, 'templates')],
                                    'APP_DIRS'  :   True,
                                    'OPTIONS'   :   {
                                                        'context_processors': 
                                                        [
                                                            'django.template.context_processors.debug',
                                                            'django.template.context_processors.request',
                                                            'django.contrib.auth.context_processors.auth',
                                                            'django.contrib.messages.context_processors.messages',
                                                        ],
                                                    },
                                },
                            ]

WSGI_APPLICATION        = 'configuracion.wsgi.application'

# Add these at the top of your settings.py
load_dotenv()

# Replace the DATABASES section of your settings.py with this
tmpPostgres = urlparse(os.getenv("DATABASE_URL"))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': tmpPostgres.path.replace('/', ''),
        'USER': tmpPostgres.username,
        'PASSWORD': tmpPostgres.password,
        'HOST': tmpPostgres.hostname,
        'PORT': 5432,
        'OPTIONS': dict(parse_qsl(tmpPostgres.query)),
    }
}

# DATABASES               =   {
#                                 'default'   :   {
#                                                     'ENGINE':           'django.db.backends.postgresql',
#                                                     'NAME':             config('DB_PRINCIPAL'),
#                                                     'USER':             config('USUARIO_DESARROLLO'),
#                                                     'PASSWORD':         config('CLAVE_DESARROLLO'),
#                                                     'HOST':             config('IP_DESARROLLO'),
#                                                     'PORT':             config('PUERTO_PREDETERMINADO'),
#                                                     # PARA LEER CON InspectDB un esquema especifico
#                                                     #'OPTIONS': {'options': '-c search_path=planteles'}
#                                                 },
#                                 'geo_db' :    {
#                                                     'ENGINE':   'django.db.backends.postgresql',
#                                                     'NAME':     config('DB_GEO'),
#                                                     'USER':     config('USUARIO_DESARROLLO'),
#                                                     'PASSWORD': config('CLAVE_DESARROLLO'),
#                                                     'HOST':     config('IP_DESARROLLO'),
#                                                     'PORT':     config('PUERTO_PREDETERMINADO'),
#                                                     #"ATOMIC_REQUESTS":  config('ATOMIC_REQUESTS'),
#                                                     # PARA LEER CON InspectDB un esquema especifico
#                                                     #'OPTIONS': {'options': '-c search_path=reclamo'}
#                                                 },
#                             }

# DATABASE_ROUTERS        =   (
#                                 'conexiones.saime.SaimeRouter',
#                                 'conexiones.geo.GeoRouter',
#                             )

AUTH_USER_MODEL         = 'cuenta.User'

AUTH_PASSWORD_VALIDATORS =  [
                                { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',   },
                                { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',             },
                                { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',            },
                                { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',           },
                            ]


LANGUAGE_CODE           = 'es-ve'
TIME_ZONE               = 'America/Caracas'
USE_I18N                = True
USE_TZ                  = True
DEFAULT_AUTO_FIELD      = 'django.db.models.BigAutoField'

STATIC_URL              = 'static/'
STATICFILES_DIRS        = [os.path.join(BASE_DIR, 'staticfiles/'),]
#STATIC_ROOT            = os.path.join(BASE_DIR, 'staticfiles/')
STATIC_ROOT             = os.path.join(BASE_DIR, 'static', )
MEDIA_ROOT              = os.path.join(BASE_DIR, 'media/')
MEDIA_URL               = '/media/'



CORS_ALLOW_ALL_ORIGINS  =   True # Si esta en True acepta peticiones de cualquier origen 
                            # Si esta en True entonces `CORS_ALLOWED_ORIGINS` no tendra efecto
CORS_ALLOW_CREDENTIALS  =   False


# Logging Configuration
# Clear prev config
LOGGING_CONFIG = None

# Get log_level from env
LOG_LEVEL = os.getenv("DJANGO_LOG_LEVEL", "info").upper()

logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters":   {
                            "console":  {
                                            "format": "%(asctime)s %(levelname)s [%(name)s:%(lineno)s] %(module)s %(process)d %(thread)d %("
                                            "message)s",
                                        },
                        },
        "handlers":     {
                            "console": 
                                        {
                                            "class": "logging.StreamHandler",
                                            "formatter": "console",
                                        },
                        },
        "loggers":      {
                            "":         {
                                            "level": LOG_LEVEL,
                                            "handlers": ["console",],
                                        },
                        },
    }
)

# Configuracion del SWagger
SWAGGER_SETTINGS =  {
                        "USE_SESSION_AUTH": False,
                        "api_version":      "0.1",
                        "SECURITY_DEFINITIONS": {"api_key": {"type": "apiKey", "name": "Authorization", "in": "header"},},
                    }

# Configuracion de CELERY
REDIS_URL                       =   os.getenv("BROKER_URL", "redis://localhost:6379")
CELERY_BROKER_URL               =   REDIS_URL
CELERY_BROKER_TRANSPORT_OPTIONS =   {
                                        "visibility_timeout": 3600,  # 1 hour
                                    }
CELERY_ACCEPT_CONTENT           =   ["application/json"]
CELERY_TASK_SERIALIZER          =   "json"
CELERY_RESULT_SERIALIZER        =   "json"
CELERY_TIMEZONE                 =   TIME_ZONE


#NINJA_JWT                       = {'TOKEN_OBTAIN_PAIR_INPUT_SCHEMA': 'apps.cuenta.views.token.MyTokenObtainPairInputSchema',}
# Configuracion del uso de JWT
NINJA_JWT                       =   {
                                        'ACCESS_TOKEN_LIFETIME':    timedelta(minutes=5),
                                        'REFRESH_TOKEN_LIFETIME':   timedelta(days=1),
                                        'ROTATE_REFRESH_TOKENS':    False,
                                        'BLACKLIST_AFTER_ROTATION': True,
                                        'UPDATE_LAST_LOGIN':        True,

                                        'ALGORITHM':                'HS256',
                                        'SIGNING_KEY':              config('SECRET_KEY'),
                                        'VERIFYING_KEY':            None,
                                        'AUDIENCE':                 None,
                                        'ISSUER':                   None,
                                        'JWK_URL':                  None,
                                        'LEEWAY':                   0,

                                        'USER_ID_FIELD':            'id',
                                        'USER_ID_CLAIM':            'user_id',
                                        'USER_AUTHENTICATION_RULE': 'ninja_jwt.authentication.default_user_authentication_rule',

                                        'AUTH_TOKEN_CLASSES':       ('ninja_jwt.tokens.AccessToken',),
                                        'TOKEN_TYPE_CLAIM':         'token_type',
                                        'TOKEN_USER_CLASS':         'ninja_jwt.models.TokenUser',

                                        'JTI_CLAIM':                        'jti',

                                        'SLIDING_TOKEN_REFRESH_EXP_CLAIM':  'refresh_exp',
                                        'SLIDING_TOKEN_LIFETIME':           timedelta(minutes=5),
                                        'SLIDING_TOKEN_REFRESH_LIFETIME':   timedelta(days=1),

                                        # For Controller Schemas
                                        # FOR OBTAIN PAIR
                                        'TOKEN_OBTAIN_PAIR_INPUT_SCHEMA':           "ninja_jwt.schema.TokenObtainPairInputSchema",
                                        'TOKEN_OBTAIN_PAIR_REFRESH_INPUT_SCHEMA':   "ninja_jwt.schema.TokenRefreshInputSchema",
                                        # FOR SLIDING TOKEN
                                        'TOKEN_OBTAIN_SLIDING_INPUT_SCHEMA':        "ninja_jwt.schema.TokenObtainSlidingInputSchema",
                                        'TOKEN_OBTAIN_SLIDING_REFRESH_INPUT_SCHEMA':"ninja_jwt.schema.TokenRefreshSlidingInputSchema",

                                        'TOKEN_BLACKLIST_INPUT_SCHEMA':             "ninja_jwt.schema.TokenBlacklistInputSchema",
                                        'TOKEN_VERIFY_INPUT_SCHEMA':                "ninja_jwt.schema.TokenVerifyInputSchema",
                                    }
