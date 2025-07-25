class AulaRouter:
    """
    Enrutador de los modelos en la aplicacion AULA
    """
    def db_for_read(self, model, **hints):
        """
        Lectura aplicacion AULA.
        """
        if model._meta.app_label == 'aula':
            return 'aula_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Escrituta aplicacion AULA.
        """
        if model._meta.app_label == 'aula':
            return 'aula_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Relaciones en la aplicacion AULA.
        """
        if obj1._meta.app_label == 'aula' or \
           obj2._meta.app_label == 'aula':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Migraciones en la aplicacion AULA.
        database.
        """
        if app_label == 'aula':
            return db == 'aula_db'
        return None