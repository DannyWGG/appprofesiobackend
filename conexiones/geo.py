class GeoRouter:
    """
    Enrutador de los modelos en la aplicacion SAIME
    """
    def db_for_read(self, model, **hints):
        """
        Lectura aplicacion SAIME.
        """
        if model._meta.app_label == 'geo':
            return 'geo_db'
        return None