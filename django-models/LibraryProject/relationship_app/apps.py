from django.apps import AppConfig


class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'

def ready(self):
        # Only import signals if needed
        pass
        # import relationship_app.signals


