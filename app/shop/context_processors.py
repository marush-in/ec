from .models import Settings


def get_settgins(request):
    settings = Settings.objects.first()
    return dict(settings=settings)
