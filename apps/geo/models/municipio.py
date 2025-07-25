from django.db              import models
from apps.geo.models.estado import Estado

class Municipio(models.Model):
    estado_me_id        = models.IntegerField('Estado ME ID',       blank = True, null = True)
    id                  = models.IntegerField('ID',                 primary_key = True)
    estado_cne_id       = models.IntegerField('Estado CNE ID',      blank = True, null = True)
    municipio_cne_id    = models.IntegerField('Municipio CNE ID',   blank = True, null = True)
    estado_ine_id       = models.IntegerField('Estado INE ID',      blank = True, null = True)
    municipio_ine_id    = models.IntegerField('Municipio INE ID',   blank = True, null = True)
    estado_nombre       = models.CharField('Estado',                max_length = 100, blank = True, null = True)
    estado_capital      = models.CharField('Capital del estado',    max_length = 100, blank = True, null = True)
    nombre              = models.CharField('Nombre',                max_length = 100, blank = True, null = True)
    capital             = models.CharField('Capital',               max_length = 100, blank = True, null = True)

    class Meta:
        managed             = False
        db_table            = 'geo\".\"municipio'
        verbose_name        = 'Municipio'
        verbose_name_plural = 'Municipios'

    def __str__(self):
        return self.nombre