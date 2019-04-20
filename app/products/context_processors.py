from .models import Brand


def get_products_info(request):
    brand_list = Brand.objects.all()
    return dict(
        brand_list=brand_list,
    )
