import uuid

from django.db import models


class Author(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(verbose_name='name', max_length=100, null=False, blank=False)
    surname = models.CharField(verbose_name='surname', max_length=100, null=False, blank=False)
    middle_name = models.CharField(verbose_name='middle_name', max_length=100, null=False, blank=False)

    def __str__(self):
        return f'{self.surname} {self.name} {self.middle_name}'


class Book(models.Model):
    LANGUAGES = (
        ('ru', 'russian'),
        ('en', 'english')
    )
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(verbose_name='book title', max_length=100, null=False, blank=False)
    language = models.CharField(verbose_name='language', choices=LANGUAGES, max_length=10, null=False, blank=False)
    publication_year = models.IntegerField(verbose_name='year of publication', null=False, blank=False)
    author = models.ManyToManyField(Author)


class Subscriber(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(verbose_name='name', max_length=100, null=False, blank=False)
    surname = models.CharField(verbose_name='surname', max_length=100, null=False, blank=False)
    middle_name = models.CharField(verbose_name='middle_name', max_length=100, null=False, blank=False)
    email = models.EmailField(verbose_name='email', max_length=200, null=False, blank=False)
