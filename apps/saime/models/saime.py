from django.db			  import models

class Saime(models.Model):
	id 						= models.BigAutoField('ID', 							primary_key=True)
	origen 					= models.CharField('Origen', 				max_length = 1, 	blank = False, 	null = False)
	cedula 					= models.IntegerField('Cédula', 								blank = False, 	null = False, unique = True)
	pais_origen 			= models.CharField('Pais', 					max_length=3, 		blank = True,  	null = True)
	nacionalidad 			= models.CharField('Nacionalidad', 			max_length = 4, 	blank = False, 	null = False)
	primer_nombre 			= models.CharField('Nombre', 				max_length = 100, 	blank = False, 	null = False)
	segundo_nombre 			= models.CharField('S. Nombre', 			max_length = 100,	blank = True,  	null = True)
	primer_apellido 		= models.CharField('Apellido', 				max_length = 100, 	blank = False, 	null = False)
	segundo_apellido 		= models.CharField('S.Apellido', 			max_length = 100,	blank = True, 	null = True)
	fecha_nacimiento 		= models.DateField('F. nacimiento', 							blank = False, 	null = False)
	naturalizado 			= models.SmallIntegerField(										blank = True, 	null = True)
	sexo 					= models.CharField('Sexo', 					max_length = 1,		blank = False, 	null = False)
	fecha_registro 			= models.CharField('Fecha Registro',		max_length=10, 		blank = True, 	null = True)
	fecha_ult_actualizacion = models.CharField('Fecha Actualizacion', 	max_length=10, 		blank = True, 	null = True)

	class Meta:
		managed 			= False
		db_table			= 'saime\".\"saime'
		verbose_name		= 'Saime'
		verbose_name_plural = 'Saime'

	def __str__(self):
		return "{0}".format(self.cedula)