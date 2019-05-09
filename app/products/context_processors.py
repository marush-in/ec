from .models import Brand, Category


def get_products_info(request):
    brand_list = Brand.objects.order_by('-created_at')[:10]
    category_list = Category.objects.order_by('-created_at')[:10]
    return dict(
        brand_list=brand_list,
        category_list=category_list,
    )
