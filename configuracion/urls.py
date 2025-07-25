from django.contrib             import admin
from django.urls                import path

from django.conf.urls.static    import static
from django.conf                import settings

from apps.frontend.views        import inicio

from .api import api

urlpatterns =   [
                    path('',            inicio,             name = 'inicio'             ),
                    path("admin/",      admin.site.urls),
                    path("",            api.urls),
                ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
