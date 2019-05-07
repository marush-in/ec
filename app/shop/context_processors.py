from .models import Settings
from blog.models import Category
from products.models import Like


def get_settgins(request):
    settings = Settings.objects.first()
    categories = Category.objects.order_by('-created_at')[:5]
    number_likes = 0
    if request.user.is_authenticated:
        number_likes = Like.objects.filter(user=request.user).count()
    return dict(
        settings=settings,
        categories=categories,
        number_likes=number_likes,
    )
