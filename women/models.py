from django.db import models
from django.contrib.auth import get_user_model
from mptt.models import MPTTModel, TreeForeignKey
from women.managers import WomenManager

User = get_user_model()


class Women(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь',
                                null=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    objects = WomenManager()

    def __str__(self):
        return f'{self.user} {self.content} {self.cat}'


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


class Genre(MPTTModel):
    women = models.ForeignKey(Women, on_delete=models.CASCADE, null=True, blank=True, related_name='w')
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='wom')

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']
