import factory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyText, FuzzyInteger

from common.factories import Faker
from .models import Category, Brand, Product


class ProductCategoryFactory(DjangoModelFactory):
    name = FuzzyText(length=15)
    slug = FuzzyText(length=15)
    image = factory.django.ImageField(
        color='green',
        height=240,
        width=350,
    )

    class Meta:
        model = Category


class BrandFactory(DjangoModelFactory):
    name = FuzzyText(length=15)
    slug = FuzzyText(length=15)
    logo = factory.django.ImageField(
        color='black',
        height=24,
        width=100,
    )

    class Meta:
        model = Brand


class ProductFactory(DjangoModelFactory):
    name = Faker('sentence')
    description = Faker('sentence')
    slug = FuzzyText(length=15)
    category = factory.Iterator(Category.objects.all())
    brand = factory.Iterator(Brand.objects.all())
    image = factory.django.ImageField(
        color='green',
        height=1300,
        width=1000,
    )
    image2 = factory.django.ImageField(
        color='yellow',
        height=1300,
        width=1000,
    )
    image3 = factory.django.ImageField(
        color='white',
        height=1300,
        width=1000,
    )
    price = FuzzyInteger(1000, 10000)
    stock = FuzzyInteger(1, 30)

    class Meta:
        model = Product
