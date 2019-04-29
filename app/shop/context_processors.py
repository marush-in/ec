from .models import Settings
from blog.models import Category


def get_settgins(request):
    settings = Settings.objects.first()
    categories = Category.objects.order_by('-created_at')[:5]
    return dict(
        settings=settings,
        categories=categories,
    )
