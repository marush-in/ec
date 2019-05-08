from .models import Settings
from blog.models import Category
from products.models import Like


def get_settgins(request):
    settings = Settings.objects.first()
    categories = Category.objects.order_by('-created_at')[:5]
    number_likes = 0
    liked_products = []
    if request.user.is_authenticated:
        user = request.user
        number_likes = Like.objects.filter(user=user).count()
        likes = Like.objects.filter(user=user)
        if likes:
            liked_products = [like.product_id for like in likes]
    return dict(
        settings=settings,
        categories=categories,
        number_likes=number_likes,
        liked_products=liked_products,
    )
