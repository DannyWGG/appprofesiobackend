from django.db import models

class Comunidade(models.Model):
    estado_me_id                        = models.IntegerField('Estado ME ID',           blank = True, null = True)
    municipio_me_id                     = models.IntegerField('Municipio ME ID',        blank = True, null = True)
    parroquia_me_id                     = models.IntegerField('parroquia ME ID',        blank = True, null = True)
    comunidad_me_id                     = models.IntegerField('Comunidad ME ID',        blank = True, null = True)
    estado_cne_id                       = models.IntegerField('Estado CNE ID',          blank = True, null = True)
    municipio_cne_id                    = models.IntegerField('Municipio CNE ID',       blank = True, null = True)
    parroquia_cne_id                    = models.IntegerField('Parroquia CNE ID',       blank = True, null = True)
    comunidad_cne_id                    = models.BigIntegerField('Comunidad CNE ID',    blank = True, null = True)
    estado_ine_id                       = models.IntegerField('Estado INE ID',          blank = True, null = True)
    municipio_ine_id                    = models.IntegerField('Municipio INE ID',       blank = True, null = True)
    parroquia_ine_id                    = models.IntegerField('Parroquia INE ID',       blank = True, null = True)
    comunidad_ine_id                    = models.BigIntegerField('Comunidad INE ID',    blank = True, null = True)
    codigo_unico_parroquia              = models.IntegerField('CU. Parroquia',          blank = True, null = True)
    codigo_unico_parroquia_comunidad    = models.IntegerField('CU. PC',                 blank = True, null = True)
    estado_nombre                       = models.CharField('Estado',                    blank = True, null = True, max_length = 100)
    estado_capital                      = models.CharField('Capital del estado',        blank = True, null = True, max_length = 100)
    municipio_nombre                    = models.CharField('Municipio',                 blank = True, null = True, max_length = 100)
    municipio_capital                   = models.CharField('Capital del Municipio',     blank = True, null = True, max_length = 100)
    parroquia_nombre                    = models.CharField('Parroquia',                 blank = True, null = True, max_length = 100)
    nombre                              = models.CharField('Comunidad',                 blank = True, null = True, max_length = 100)
    id                                  = models.IntegerField('ID',                     primary_key = True)

    class Meta:
        managed             = False
        db_table            = 'geo\".\"comunidad'
        verbose_name        = 'Comunidad'
        verbose_name_plural = 'Comunidades'

    def __str__(self):
        return self.nombre