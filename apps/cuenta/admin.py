from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.utils.html import format_html
from .models import User
from django.contrib.auth.models import Group

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email',)

class CustomUserAdmin(UserAdmin):
    # Acciones editadas para el admin estándar
    def editar(self, obj):
        return format_html(
            '<a class="button" href="/admin/cuenta/user/{}/change/">Editar</a>',
            obj.id
        )
    
    def eliminar(self, obj):
        return format_html(
            '<a class="button" href="/admin/cuenta/user/{}/delete/" style="color:red;">Eliminar</a>',
            obj.id
        )

    add_form = UserCreateForm
    prepopulate_fields = {'username': ('origen', 'cedula', 'email',)}
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'origen', 'cedula', 'primer_nombre', 
                      'email', 'estado', 'password1', 'password2')
        }),
    )
    
    readonly_fields = [
        'pregunta_01', 'pregunta_02', 'pregunta_03',
        'respuesta_01', 'respuesta_02', 'respuesta_03',
        'last_login', 'fecha_registro', 'is_superuser'
    ]
    
    list_display = ('username', 'cedula', 'email', 'estado', 'editar', 'eliminar')
    list_filter = ('username', 'cedula', 'email', 'estado')
    list_display_links = None
    
    fieldsets = (
        ('Credenciales', {
            'fields': ('username', 'origen', 'cedula', 'primer_nombre', 
                      'email', 'estado', 'password')
        }),
        ('Recuperación', {
            'fields': ('pregunta_01', 'pregunta_02', 'pregunta_03',
                      'respuesta_01', 'respuesta_02', 'respuesta_03')
        }),
        ('Permisos', {
            'fields': ('is_staff', 'is_active', 'groups')
        }),
        ('Actividad', {
            'fields': ('fecha_registro', 'last_login')
        }),
    )

# Registro del modelo
admin.site.register(User, CustomUserAdmin)