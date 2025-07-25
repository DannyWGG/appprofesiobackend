from django.contrib                     import admin
from django.contrib                     import messages
from django.utils.translation           import ngettext
from django.utils.html 			        import format_html

from apps.saime.models.saime        import Saime

#admin.site.disable_action("delete_selected")

@admin.register(Saime)
class SaimeAdmin(admin.ModelAdmin):
    @admin.action(permissions  = ["change"])
    def desactivar(self, request, queryset):
        desactivados = queryset.update(estatus = 'False')
        self.message_user(request, ngettext("%d Operación Exitosa", "%d Operación Exitosa", desactivados)
        % desactivados, messages.SUCCESS)

    @admin.action(permissions  = ["change"])
    def reactivar(self, request, queryset):
        reactivados = queryset.update(estatus = 'True')
        self.message_user(request, ngettext("%d Operación Exitosa", "%d Operación Exitosa", reactivados)
        % reactivados, messages.SUCCESS)

    # Accesos directos del lado derecho
    @admin.action(permissions  = ["change"])
    def editar(self, obj):
        return format_html('<a class="btn" href="/admin/saime/saime/{}/change/"><i class="nav-icon fas fa-edit"></i></a>', obj.id)
    
    @admin.action(permissions  = ["delete"])
    def eliminar(self, obj):
        return format_html('<a class="btn" href="/admin/saime/saime/{}/delete/"><i class="nav-icon fas fa-trash"></i></a>', obj.id)

    list_display        = ('origen','cedula','pais_origen','nacionalidad','primer_nombre','segundo_nombre','primer_apellido','segundo_apellido','fecha_nacimiento','sexo','fecha_registro','fecha_ult_actualizacion','editar','eliminar','id')
    list_filter         = []
    search_fields       = []
    list_display_links  = None
    actions             = [desactivar, reactivar]
    list_select_related = True