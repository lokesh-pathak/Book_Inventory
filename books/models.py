from django.db import models


class DefaultDateModel(models.Model):
    """ Abstract model class to created_at and updated_at fields """

    crd = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    upd = models.DateTimeField(auto_now=True, null=True, blank=True)
    objects = models.Manager()  # The default manager.

    class Meta:
        abstract = True


class Category(DefaultDateModel):
    name = models.CharField(db_index=True, max_length=200)

    class Meta:
        db_table = 'category'


# Create your models here.
class Inventory(DefaultDateModel):
    """docstring for inventory"""
    book_name = models.CharField(db_index=True, max_length=200)
    description = models.TextField(null=True, blank=True)
    categories = models.ManyToManyField(Category)

    class Meta:
        db_table = 'inventory'
