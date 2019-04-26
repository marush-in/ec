import factory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyText

from common.factories import Faker
from .models import Category, Post, PopularPost


class CategoryFactory(DjangoModelFactory):
    name = FuzzyText(length=15)
    slug = FuzzyText(length=15)

    class Meta:
        model = Category


class PostFactory(DjangoModelFactory):
    title = Faker('sentence')
    description = Faker('sentence')
    slug = FuzzyText(length=15)
    category = factory.Iterator(Category.objects.all())
    eyecatch = eyecatch = factory.django.ImageField(
        color='blue',
        height=290,
        width=540,
    )
    content = FuzzyText(length=2000)
    is_published = True

    class Meta:
        model = Post


class PopularPostFactory(DjangoModelFactory):
    post = factory.Iterator(Post.objects.all())

    class Meta:
        model = PopularPost
