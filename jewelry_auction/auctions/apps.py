from django.apps import AppConfig

class AuctionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auctions'

    def ready(self):
        from .scheduler import start_scheduler
        start_scheduler()