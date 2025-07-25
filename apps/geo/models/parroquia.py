from django.db                  import models
from apps.geo.models.estado     import Estado
from apps.geo.models.municipio  import Municipio

class Parroquia(models.Model):
    id                  = models.IntegerField('ID',                 primary_key = True)
    estado_me_id        = models.IntegerField('Estado ME ID',       blank = True, null = True)
    municipio_me_id     = models.IntegerField('Municipio ME ID',    blank = True, null = True)
    parroquia_me_id     = models.IntegerField('Parroquia ME ID',    blank = True, null = True)
    estado_cne_id       = models.IntegerField('Estado CNE ID',      blank = True, null = True)
    municipio_cne_id    = models.IntegerField('Municipio CNE ID',   blank = True, null = True)
    parroquia_cne_id    = models.IntegerField('Parroquia CNE ID',   blank = True, null = True)
    estado_ine_id       = models.IntegerField('Estado CNE ID',      blank = True, null = True)
    municipio_ine_id    = models.IntegerField('Municipio INE ID',   blank = True, null = True)
    parroquia_ine_id    = models.IntegerField('Parroquia INE ID',   blank = True, null = True)
    nombre              = models.CharField('Nombre',                blank = True, null = True, max_length = 100)

    class Meta:
        managed             = False
        db_table            = 'geo\".\"parroquia'
        verbose_name        = 'Parroquia'
        verbose_name_plural = 'Parroquias'

    def __str__(self):
        return self.nombre