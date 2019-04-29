from .models import Brand


def get_products_info(request):
    brand_list = Brand.objects.order_by('-created_at')[:10]
    return dict(
        brand_list=brand_list,
    )
