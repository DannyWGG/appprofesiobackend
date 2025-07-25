from django.urls            import path
from apps.saime.views.saime import consulta

urlpatterns =   [
                    path('<str:origen>/<int:cedula>/',   consulta,      name = 'consulta'    ),
                ]