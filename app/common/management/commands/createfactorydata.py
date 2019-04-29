from django.core.management import BaseCommand
from django.db import transaction

from blog.factories import (
    PostCategoryFactory,
    PostFactory,
    PopularPostFactory,
)
from products.factories import (
    ProductCategoryFactory,
    BrandFactory,
    ProductFactory,
    PopularProductFactory
)


class Command(BaseCommand):
    help = 'Create factory data.'

    @transaction.atomic()
    def handle(self, *args, **options):
        PostCategoryFactory.create_batch(10)
        PostFactory.create_batch(20)
        PopularPostFactory.create_batch(5)
        ProductCategoryFactory.create_batch(10)
        BrandFactory.create_batch(10)
        ProductFactory.create_batch(20)
        PopularProductFactory.create_batch(10)
