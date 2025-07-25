from django.db import models

class Estado(models.Model):
    id              = models.IntegerField('estado ME ID',                        primary_key = True, )
    estado_cne_id   = models.IntegerField('Estado CNE ID',                  blank = True, null = True)
    estado_ine_id   = models.IntegerField('Estado INE ID',                  blank = True, null = True)
    nombre          = models.CharField('Nombre',            max_length=100, blank = True, null = True)
    capital         = models.CharField('Capital',           max_length=100, blank = True, null = True)

    class Meta:
        managed             = False
        db_table            = 'geo\".\"estado'
        verbose_name        = 'Estado'
        verbose_name_plural = 'Estados'

    def __str__(self):
        return self.nombre